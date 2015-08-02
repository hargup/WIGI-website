from __future__ import print_function
from collections import OrderedDict
from bokeh.plotting import figure, output_file
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.resources import CDN
from bokeh.embed import autoload_static


def load_data(data_file):
    import csv
    lang_data = dict()
    with open(data_file, 'r') as csvfile:
        indexreader = csv.reader(csvfile)
        for code, gendered_total, fem_percent, name in indexreader:
            lang_data[code] = {"gendered_total": int(gendered_total),
                               "fem_percent": float(fem_percent),
                               "name": name}
    return lang_data


def plot():
    lang_data = load_data('./data/language_by_gender.csv')

    gendered_total = [lang_data[code]['gendered_total']
                      for code in lang_data.keys()]
    fem_percent = [lang_data[code]['fem_percent'] for code in lang_data.keys()]
    lang_name = [lang_data[code]['name'] for code in lang_data.keys()]

    source = ColumnDataSource(
            data=dict(
                lang_name=lang_name,
                gendered_total=gendered_total,
                fem_percent=fem_percent
                )
            )

    TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

    p = figure(x_axis_type="log", x_range=[0.1, 10**6], y_range=[0, 1],
               title="Language by Gender", tools=TOOLS)

    # TODO: We can potentially choose the color of the circle by the culture of
    # the language, and maybe we can represent the size of the circle by the
    # number of speakers

    x = gendered_total
    y = fem_percent
    p.scatter(x, y, size=20, color="#74bc3a", source=source)
    p.text(x, y, text=lang_name, text_color="#ff9944", text_align="center")

    p.xaxis.axis_label = "Total Number of Gendered Biographies"

    p.yaxis.axis_label = "Percentage of Female Biographies"
    p.yaxis.formatter = NumeralTickFormatter(format="0.0%")

    hover = p.select(dict(type=HoverTool))
    hover.point_policy = "follow_mouse"
    hover.tooltips = OrderedDict([
        ("Language", "@lang_name"),
        ("Total gendered biographies", "@gendered_total"),
        ("Percentage Female biographies", "@fem_percent")
    ])

    js_filename = "language_by_gender.js"
    output_path = "./files/assets/js/"
    script_path = "../assets/js/"

    # generate javascript plot and corresponding script tag
    js, tag = autoload_static(p, CDN, script_path + js_filename)

    with open(output_path + js_filename, 'w') as js_file:
        js_file.write(js)

    return tag


if __name__ == "__main__":
    print(plot())
