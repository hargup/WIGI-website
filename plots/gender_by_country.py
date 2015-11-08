from __future__ import print_function
from collections import OrderedDict

import numpy as np
import pandas as pd
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure

from . import world_countries as wc
from .utils import write_plot, read_data


@write_plot('country')
def plot(newest_changes):
    df, date_range = read_data(newest_changes, 'worldmap')

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

    # setup widgets and figure
    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
    p = figure(plot_width=800, plot_height=500, tools=TOOLS)

    p.patches(country_xs, country_ys, fill_color=colors, source=source)

    # hide axes
    p.axis.visible = None

    hover = p.select(dict(type=HoverTool))
    hover.point_policy = "follow_mouse"

    # change tooltip according to plot type
    if newest_changes == 'newest-changes':
        hover.tooltips = OrderedDict([
            ("Change in WIGI", "@wigi_index"),
            ("Country", "@name"),
        ])
    else:
        hover.tooltips = OrderedDict([
            ("WIGI", "@wigi_index"),
            ("Country", "@name"),
        ])


    # FIX: generate top and bottom tables, currently uses older dataframe
    major = df[df['total'] > 100]
    labels = [i for i in major.index if i in world_countries.keys()]
    major = major.loc[labels]
    major.rename(dict((code, world_countries[code]['name'])
                      for code in labels), inplace=True)
    sorted_major = major.sort_values('Score', ascending=False)
    sorted_major.columns = ['Total', 'Score']
    top_rows = sorted_major.head(10).to_html(classes=['table'])
    bottom_rows = sorted_major[::-1].head(10).to_html(classes=['table'])

    table_html = [top_rows, bottom_rows]

    return p, date_range, table_html

if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
