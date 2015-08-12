from __future__ import print_function
from collections import OrderedDict
from bokeh.plotting import figure, output_file
from bokeh.charts import Scatter, output_notebook, show
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.resources import CDN
from bokeh.embed import autoload_static
import os
import pandas


def plot(newest_changes):
    filelist = os.listdir('/home/maximilianklein/snapshot_data/{}/'.format(newest_changes))
    site_linkss_file = [f for f in filelist if f.startswith('site_linkss')][0]
    if newest_changes == 'newest-changes':
        date_range = site_linkss_file.split('site_linkss-index-from-')[1].split('.csv')[0].replace('-',' ')
    csv_to_read = '/home/maximilianklein/snapshot_data/{}/{}'.format(newest_changes,site_linkss_file)
    df = pandas.DataFrame.from_csv(csv_to_read)
    no_gender_perc = df['nan'].sum() / df.sum().sum()
    print('no gender %', no_gender_perc)
    del df['nan']
    df['total'] = df.sum(axis=1)
    df['nonbin'] = df['total'] - df['male'] - df['female']
    df['fem_per'] = df['female'] / (df['total'])
    df['nonbin_per'] = df['nonbin'] / df['total']
    dfs = df.sort('total')


    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
    
    title_suffix = 'Changes since {}'.format(date_range) if newest_changes == 'newest-changes' else 'All Time'
    p = figure(x_axis_type="log", x_range=[0.1, 10**6], y_range=[0, 1],
               title="Language by Gender {}".format(title_suffix), tools=TOOLS)

    p.circle(dfs['total'], dfs['fem_per'], size=12, line_color="black", fill_alpha=0.8)

    p.text(dfs["total"]+0.001, dfs["fem_per"]+0.001,
        text=dfs.index,text_color="#333333",
        text_align="center", text_font_size="10pt")

    hover = p.select(dict(type=HoverTool))
    hover.point_policy = "follow_mouse"
    hover.tooltips = OrderedDict([
        ("Language", "@lang_name"),
        ("Total gendered biographies", "@gendered_total"),
        ("Percentage Female biographies", "@fem_percent")
    ])

    js_filename = "gender_by_language_{}.js".format(newest_changes)
    output_path = "./files/assets/js/"
    script_path = "./assets/js/"

    # generate javascript plot and corresponding script tag
    js, tag = autoload_static(p, CDN, script_path + js_filename)

    with open(output_path + js_filename, 'w') as js_file:
        js_file.write(js)

    return tag


if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
