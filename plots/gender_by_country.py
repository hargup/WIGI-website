from __future__ import print_function
from collections import OrderedDict
import csv
import numpy as np
import pandas as pd
from . import world_countries as wc
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import autoload_static
import os
from .config import data_dir
from .utils import get_date_range

def plot(newest_changes):
    filelist = os.listdir('{}/{}/'.format(data_dir, newest_changes))
    site_linkss_file = [f for f in filelist if f.startswith('worldmap')][0]
    date_range = ""
    if newest_changes == 'newest-changes':
        start, end = site_linkss_file.split('worldmap-index-from-')[1].split('.csv')[0].split('-to-')
        date_range = get_date_range(start, end)
        print(date_range)
    csv_to_read = '{}/{}/{}'.format(data_dir, newest_changes,site_linkss_file)
    df = pd.DataFrame.from_csv(csv_to_read)

    # drop 'NaN' rows
    df = df[list(map(lambda x: not pd.isnull(x), df.index))]

    # https://github.com/chdoig/pyladiesatx-bokeh-tutorial
    world_countries = wc.data.copy()

    country_xs = [world_countries[code]['lons'] for code in world_countries]
    country_ys = [world_countries[code]['lats'] for code in world_countries]
    country_names = [world_countries[code]['name'] for code in world_countries]

    def lookup_wigi(code):
        try:
            return df.ix[code]['Score']
        except KeyError:
            return -1

    # TODO: adjust the scale for the changes plot
    index_vals = np.array([lookup_wigi(code) for code in world_countries])

    def fmt(c):
        return int(np.nan_to_num(c))

    # TODO: Pick better colors
    colors = [
        "#%02x%02x%02x" % (fmt(r), fmt(g), fmt(b)) for r, g, b in
        zip(np.floor(87 - 80*2*(-0.5 + 1/(1 + np.exp(-3*index_vals)))),
            np.floor(150 - 150*2*(-0.5 + 1/(1 + np.exp(-3*index_vals)))),
            np.floor(118 - 100*2*(-0.5 + 1/(1 + np.exp(-3*index_vals)))))]

    source = ColumnDataSource(
            data=dict(
                    name=country_names,
                    wigi_index=[str(idx) for idx in index_vals]
                )
            )

    # setup widgets
    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
    title_suffix = 'Changes since {}'.format(date_range) if newest_changes == 'newest-changes' else 'All Time'

    p = figure(title="Gender by Country {}".format(title_suffix), tools=TOOLS,
               plot_width=800, plot_height=500)

    p.patches(country_xs, country_ys, fill_color=colors, source=source)

    hover = p.select(dict(type=HoverTool))
    hover.point_policy = "follow_mouse"
    hover.tooltips = OrderedDict([
        ("wigi", "@wigi_index"),
        ("Country", "@name"),
    ])

    js_filename = "gender_by_country_{}.js".format(newest_changes)
    script_path = "./assets/js/"
    output_path = "./files/assets/js/"

    # generate javascript plot and corresponding script tag
    js, tag = autoload_static(p, CDN, script_path + js_filename)

    with open(output_path + js_filename, 'w') as js_file:
        js_file.write(js)

    # FIX: generate top and bottom tables, currently uses older dataframe
    major = df[df['total'] > 100]
    sorted_major = major.sort_values('Score', ascending=False)
    sorted_major.columns = ['Total', 'Score']
    top_rows = sorted_major.head(10).to_html(classes=['table'])
    bottom_rows = sorted_major[::-1].head(10).to_html(classes=['table'])

    return {'plot_tag':tag, 'table_html':[top_rows, bottom_rows], 'date_range': date_range}

if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
