from __future__ import print_function
from collections import OrderedDict
from bokeh.plotting import figure, output_file
from bokeh.charts import Scatter, output_notebook, show
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.resources import CDN
from bokeh.embed import autoload_static
import os
import pandas as pd
from numpy import max, min
from .config import data_dir
from .utils import get_date_range


def plot(newest_changes):
    filelist = os.listdir('{}/{}/'.format(data_dir, newest_changes))
    site_linkss_file = [f for f in filelist if f.startswith('site_linkss')][0]
    date_range = None
    if newest_changes == 'newest-changes':
        start, end = site_linkss_file.split('site_linkss-index-from-')[1].split('.csv')[0].split('-to-')
        date_range = get_date_range(start, end)
    csv_to_read = '{}/{}/{}'.format(data_dir, newest_changes,site_linkss_file)
    df = pd.DataFrame.from_csv(csv_to_read)
    no_gender_perc = df['nan'].sum() / df.sum().sum()
    print('no gender %', no_gender_perc)

    # drop 'nan' and non wiki columns
    del df['nan']
    df = df[list(map(lambda x: isinstance(x, str) and x.endswith('wiki'), df.index))]

    df['total'] = df.sum(axis=1)
    df['nonbin'] = df['total'] - df['male'] - df['female']
    df['fem_per'] = (df['female'] / (df['total']))*100
    df['nonbin_per'] = (df['nonbin'] / df['total'])*100

    # take only top 50 entries
    dfs = df.sort_values('total', ascending=False).head(50)
    fsort_dfs = dfs.sort_values('fem_per', ascending=False)
    cutoff = fsort_dfs[['total','fem_per']].reset_index()

    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save,box_select"

    title_suffix = 'Changes since {}'.format(date_range) if newest_changes == 'newest-changes' else 'All Time'

    # adjust scale
    y_max = max(cutoff['total'])*1.1
    y_min = min(cutoff['total']) - y_max*.05
    x_max = max(cutoff['fem_per'])*1.1
    x_min = min(cutoff['fem_per']) - x_max*.05

    p = figure(x_axis_type="linear", x_range=[x_min, x_max], y_range=[y_min, y_max],
               tools=TOOLS, plot_width=800, plot_height=500)

    p.xaxis.axis_label='Percentage female biographies'
    p.yaxis.axis_label='Total biographies'

    source = ColumnDataSource(data=cutoff.to_dict(orient='list'))
    p.circle('fem_per', 'total', size=12, line_color="black", fill_alpha=0.8, source=source)

    #p.text(cutoff["total"]+0.001, cutoff["fem_per"]+0.001,
           #text=cutoff.index, text_color="#333333",
           #text_align="center", text_font_size="10pt")


    # setup tools
    hover = p.select(dict(type=HoverTool))
    hover.point_policy = "follow_mouse"
    hover.tooltips = OrderedDict([
        ("Language wiki", "@index"),
        ("Total biographies", "@total"),
        ("Percentage female biographies", "@fem_per")
    ])

    js_filename = "gender_by_language_{}.js".format(newest_changes)
    output_path = "./files/assets/js/"
    script_path = "./assets/js/"

    # generate javascript plot and corresponding script tag
    js, tag = autoload_static(p, CDN, script_path + js_filename)

    with open(output_path + js_filename, 'w') as js_file:
        js_file.write(js)

    # rename columns and generate top/bottom tables
    cutoff.columns=['Wiki', 'Total','Female (%)']
    top_rows = cutoff.head(10).to_html(na_rep='n/a', classes=["table"])
    bottom_rows = cutoff[::-1].head(10).to_html(na_rep='n/a', classes=["table"])

    return {'plot_tag':tag, 'table_html':[top_rows, bottom_rows], 'date_range':
            date_range}


if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
