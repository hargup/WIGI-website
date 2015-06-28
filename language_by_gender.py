from __future__ import print_function
from bokeh.plotting import figure, output_file
from bokeh.models import NumeralTickFormatter
from bokeh.models import HoverTool, ColumnDataSource
from collections import OrderedDict
from bokeh.resources import CDN
from bokeh.embed import autoload_static

# Here we can play arond with Size of circle by making it proportional
# to the size of the resepecitive wikipedia


def load_data(data_file):
    # XXX: This is dummy data and it is possible that the original data will be
    # in some other format.
    import csv
    lang_data = dict()
    with open(data_file, 'r') as csvfile:
        indexreader = csv.reader(csvfile)
        for code, gendered_total, fem_percent, name in indexreader:
            lang_data[code] = {"gendered_total": int(gendered_total),
                               "fem_percent": float(fem_percent),
                               "name": name}
    return lang_data


def create_language_by_gender_plot():
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
    output_file("language_by_gender.html", title="Language by Gender")

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

    # Since all paths are relative and code and html file does not lie in the
    # directory, output_dir and read_dir differs
    output_dir = "./output/scripts/"
    read_dir = "./scripts/"
    js_file_name = "language_by_gender.js"
    js, tag = autoload_static(p, CDN, read_dir + js_file_name)

    with open(output_dir + js_file_name, 'w') as js_file:
        js_file.write(js)

    return tag


if __name__ == "__main__":
    print(create_language_by_gender_plot())
