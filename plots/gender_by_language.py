from __future__ import print_function
from collections import OrderedDict

from numpy import max, min
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import (HoverTool,
                          ColumnDataSource,
                          NumeralTickFormatter)

from .utils import write_plot, read_data


# The csv for language codes and their English is taken from
# http://wikistats.wmflabs.org/
wikis = pd.DataFrame.from_csv('./plots/wikipedias.csv')
langdict = dict([(code.replace('-', '_')+'wiki', name) for code, name in
                 zip(wikis.lang, wikis.id)])


@write_plot('language')
def plot(newest_changes):
    df, date_range = read_data(newest_changes, 'site_linkss')

    # Taking only wikipedias ignoring wikiquote, wikinews and wikisource
    df = df.loc[list(langdict.keys())]
    df.rename(langdict, inplace=True)

    has_changes = df.abs().sum().sum() != 0

    if not has_changes:
        return None, None, None, False

    print("has_changes %s" % (has_changes))

    no_gender_perc = df['nan'].sum() / df.sum().sum()
    print('no gender %', no_gender_perc)

    del df['nan']

    df['total'] = df.sum(axis=1)
    df['nonbin'] = df['total'] - df['male'] - df['female']
    df['fem_per'] = (df['female']*100 / (df['total'])).round(2)
    df['nonbin_per'] = (df['nonbin']*100 / df['total']).round(2)

    # take only top 50 entries
    dfs = df.sort_values('total', ascending=False).head(50)
    fsort_dfs = dfs.sort_values('fem_per', ascending=False)
    cutoff = fsort_dfs[['total', 'female', 'fem_per']].reset_index()

    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save,box_select"

    # adjust scale
    y_max = max(cutoff['total'])*1.2
    y_min = min(cutoff['total'])*0.8
    x_max = max(cutoff['fem_per'])*1.1
    x_min = min(cutoff['fem_per']) - x_max*.05

    p = figure(x_axis_type="linear", y_axis_type="log",
               x_range=[x_min, x_max], y_range=[y_min, y_max], tools=TOOLS,
               plot_width=800, plot_height=500)

    p.xaxis.axis_label = 'Percentage female biographies'
    p.yaxis.axis_label = 'Total biographies'
    p.yaxis[0].formatter = NumeralTickFormatter(format='0,0')

    source = ColumnDataSource(data=cutoff.to_dict(orient='list'))
    p.circle('fem_per', 'total', size=12, line_color="black", fill_alpha=0.8,
             source=source)

    # label text showing language name
    p.text(x="fem_per", y="total", text="index", text_color="#333333",
           text_align="left", text_font_size="8pt",
           y_offset=-5, source=source)

    # setup tools
    hover = p.select(dict(type=HoverTool))
    hover.point_policy = "follow_mouse"
    hover.tooltips = OrderedDict([
        ("Language wiki", "@index"),
        ("Total biographies", "@total"),
        ("Total female biographies", "@female"),
        ("Female biographies", "@fem_per{1.11} %")
    ])

    # rename columns and generate top/bottom tables
    cutoff.columns = ['Wiki', 'Total', 'Female', 'Female (%)']
    top_rows = cutoff.head(10)
    bottom_rows = cutoff[::-1].head(10)

    table = [top_rows, bottom_rows]

    return p, date_range, table, True


if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
