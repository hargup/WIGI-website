import pandas as pd
from bokeh.plotting import figure
from bokeh.models import HoverTool
import os
from .config import data_dir
from .utils import get_date_range, write_plot


@write_plot
def plot(newest_changes):
    dox = pd.DataFrame()
    interesante = ['female', 'male', 'nonbin', 'fem_per', 'nonbin_per']

    for l in ['b', 'd']:
        acro = 'do'+l
        filelist = os.listdir('{}/{}/'.format(data_dir, newest_changes))
        dox_list = [f for f in filelist if f.startswith(acro)]
        dox_file = dox_list[0]
        date_range = None
        if newest_changes == 'newest-changes':
            start, end = dox_file.split('{}-index-from-'.format(acro))[1].split('.csv')[0].split('-to-')
            date_range = get_date_range(start, end)
        csv_to_read = '{}/{}/{}'.format(data_dir, newest_changes,dox_file)
        df = pd.DataFrame.from_csv(csv_to_read)

        del df['nan']
        df = df[list(map(lambda x: not pd.isnull(x), df.index))]

        df['total'] = df.sum(axis=1)
        df['nonbin'] = df['total'] - df['male'] - df['female']
        df['fem_per'] = df['female'] / (df['total'])
        df['nonbin_per'] = df['nonbin'] / df['total']

        for inte in interesante:
            dox['{}-{}'.format(acro, inte)] = df[inte]

    time_range = (1500, 2015)

    dox = dox[time_range[0]: time_range[1]]

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
        ("index", "$index"),
        ("Year of event", "$x"),
        ("Number of biographies", "$y"),
    ]

    htmltable = dox[['dob-female', 'dod-female',
                     'dob-male', 'dod-male',
                     'dob-nonbin', 'dod-nonbin',
                     'dob-fem_per', 'dod-fem_per',
                     'dod-nonbin_per', 'dod-nonbin_per']].sort_values('dob-fem_per', ascending=False)

    htmltable.columns = ['DoB (Female)', 'DoD (Female)',
                         'DoB (Male)', 'DoD (Male)',
                         'DoB (Non Binary)', 'DoD (Non Binary)',
                         'DoB (Female Percentage)', 'DoD (Female Percentage)',
                         'DoB (Non Binary Percentage)', 'DoD (Non Binary Percentage)']
    top_rows = htmltable.head(10).to_html(na_rep="n/a", classes=["table"])
    bottom_rows = htmltable[::-1].head(10).to_html(na_rep="n/a", classes=["table"])
    table_html = [top_rows, bottom_rows]

    return p, date_range, table_html

if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
