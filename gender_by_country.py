import world_countries as wc
from bokeh.plotting import figure, output_file, save
import numpy as np
from bokeh.models import HoverTool, ColumnDataSource
import csv
from collections import OrderedDict
# The world countries file is taken from https://github.com/chdoig/pyladiesatx-bokeh-tutorial


world_countries = wc.data.copy()

country_xs = [world_countries[code]['lons'] for code in world_countries]
country_ys = [world_countries[code]['lats'] for code in world_countries]
country_names = [world_countries[code]['name'] for code in world_countries]

index_dict = dict()
with open('./data/gender-by-country.csv', 'r') as csvfile:
    indexreader = csv.reader(csvfile)
    for country, index in indexreader:
        index_dict[country] = float(index)

index_vals = np.array([index_dict[code] for code in world_countries])

colors = [
     "#%02x%02x%02x" % (r, g, b) for r, g, b in
     zip(np.floor(250*(1-index_vals)), np.floor(200*(1-index_vals)), np.floor(100*index_vals))
 ]

source = ColumnDataSource(
        data=dict(
                name=country_names,
                wigi_index=[str(idx) for idx in index_vals]
            )
        )

TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"
output_file("world_map.html", title="Gender by Country")
p = figure(title="world map", tools=TOOLS)

p.patches(country_xs, country_ys, line_color="blue", fill_color=colors, source=source)

hover = p.select(dict(type=HoverTool))
hover.point_policy = "follow_mouse"
hover.tooltips = OrderedDict([
    ("wigi", "@wigi_index"),
    ("Country", "@name"),
])
save(p)
