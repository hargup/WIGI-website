from __future__ import print_function

from numpy import sum, absolute
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import HoverTool

from .utils import write_plot, read_data, fix_nan_inf


@write_plot('dob')
def plot(newest_changes):
    dox = pd.DataFrame()
    interesante = ['female', 'male', 'nonbin', 'fem_per', 'nonbin_per']

    for l in ['b', 'd']:
        acro = 'do'+l
        df, date_range = read_data(newest_changes, acro)

        del df['nan']
        df = df[list(map(lambda x: not pd.isnull(x), df.index))]

        #df['total'] = df.sum(axis=1)
        df['total'] = df.apply(lambda x: sum(absolute(x)), axis=1)
        df['nonbin'] = df['total'] - df['male'] - df['female']
        df['fem_per'] = (df['female']*100 / (df['total'])).round(2)
        df['nonbin_per'] = (df['nonbin']*100 / df['total']).round(2)

        fix_nan_inf(df['fem_per'])
        fix_nan_inf(df['nonbin_per'])
        df.fillna(0, inplace=True)

        for inte in interesante:
            dox['{}-{}'.format(acro, inte)] = df[inte]

    time_range = (1600, 2015)

    dox = dox[time_range[0]: time_range[1]]

    has_changes = dox.abs().sum().sum() != 0

    if not has_changes:
        return None, None, None, False

    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
    p = figure(plot_height=500, plot_width=800, tools=TOOLS)

    p.line(dox.index, dox['dob-female'], color="red",
           line_width=2, legend="DoB (Female)")
    p.line(dox.index, dox['dod-female'], color="blue",
           line_width=2, legend="DoD (Female)")
    p.line(dox.index, dox['dob-male'], color="orange",
           line_width=2, legend="DoB (Male)")
    p.line(dox.index, dox['dod-male'], color="brown",
           line_width=2, legend="DoD (Male)")

    p.legend.orientation = 'top_left'
    p.xaxis.axis_label = 'Year'
    p.yaxis.axis_label = 'Number of biographies'

    # setup tools
    hover = p.select(dict(type=HoverTool))
    hover.point_policy = "follow_mouse"
    hover.tooltips = [
        ("Year of event", "@x"),
        ("Number of biographies", "@y"),
    ]

    htmltable = dox[['dob-female', 'dod-female',
                     'dob-male', 'dod-male',
                     'dob-nonbin', 'dod-nonbin',
                     'dob-fem_per', 'dod-fem_per',
                     'dod-nonbin_per', 'dod-nonbin_per']].sort_values('dob-fem_per', ascending=False)

    htmltable.columns = ['DoB (F)', 'DoD (F)',
                         'DoB (M)', 'DoD (M)',
                         'DoB (NB)', 'DoD (NB)',
                         'DoB (F) Percent', 'DoD (F) Percent',
                         'DoB (NB) Percent', 'DoD (NB) Percent']
    top_rows = htmltable.head(10)
    bottom_rows = htmltable[::-1].head(10)
    table = [top_rows, bottom_rows]

    return p, date_range, table, True

if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
