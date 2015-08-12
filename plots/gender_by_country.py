from __future__ import print_function
from collections import OrderedDict
import csv
import numpy as np
import pandas
import world_countries as wc
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import autoload_static
import os


def plot(newest_changes):
    filelist = os.listdir('/home/maximilianklein/snapshot_data/{}/'.format(newest_changes))
    site_linkss_file = [f for f in filelist if f.startswith('worldmap')][0]
    if newest_changes == 'newest-changes':
        date_range = site_linkss_file.split('worldmap-index-from-')[1].split('.csv')[0].replace('-',' ')
        print(date_range)
    csv_to_read = '/home/maximilianklein/snapshot_data/{}/{}'.format(newest_changes,site_linkss_file)
    df = pandas.DataFrame.from_csv(csv_to_read)
    major = df[df['total'] > 100]

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
    
    index_vals = np.array([lookup_wigi(code) for code in world_countries])

    def fmt(c):
        return int(np.nan_to_num(c))
    colors = [
        "#%02x%02x%02x" % (fmt(r), fmt(g), fmt(b)) for r, g, b in
        zip(np.floor(250*(1-index_vals)),
            np.floor(200*(1-index_vals)),
            np.floor(100*index_vals))]
    print(colors)
    
    source = ColumnDataSource(
            data=dict(
                    name=country_names,
                    wigi_index=[str(idx) for idx in index_vals]
                )
            )

    # setup widgets
    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
    title_suffix = 'Changes since {}'.format(date_range) if newest_changes == 'newest-changes' else 'All Time'

    p = figure(title="Gender by Country {}".format(title_suffix), tools=TOOLS)

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

    return tag

if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
