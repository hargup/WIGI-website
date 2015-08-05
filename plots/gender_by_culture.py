from __future__ import print_function
import csv
from bokeh.plotting import figure
from bokeh.models import NumeralTickFormatter
from bokeh.resources import CDN
from bokeh.embed import autoload_static


def load_data(data_file):
    lang_data = dict()
    with open(data_file, 'r') as csvfile:
        indexreader = csv.reader(csvfile)
        for code, gendered_total, fem_percent, name in indexreader:
            lang_data[code] = {"gendered_total": gendered_total,
                               "fem_percent": fem_percent,
                               "name": name}
    return lang_data


def plot():
    lang_data = load_data('./data/gender-by-culture.csv')

    p = figure(tools="pan,wheel_zoom,box_zoom,reset,previewsave",
               x_axis_type="log", x_range=[0.1, 10**6], y_range=[0, 1],
               title="Gender by Culture")

    cult_x = [lang_data[code]['gendered_total'] for code in lang_data.keys()]
    cult_y = [lang_data[code]['fem_percent'] for code in lang_data.keys()]
    cult_name = [lang_data[code]['name'] for code in lang_data.keys()]
    p.text(cult_x, cult_y, text=cult_name, text_color="#ff9944",
           text_align="center")

    p.scatter(cult_x, cult_y, color="#74bc3a", labels=cult_name)

    p.xaxis.axis_label = "Total number of gendered biographies"

    p.yaxis.axis_label = "Percentage of female biographies"
    p.yaxis.formatter = NumeralTickFormatter(format="0.0%")

    js_filename = "gender_by_culture.js"
    output_path = "./files/assets/js/"
    script_path = "../assets/js/"

    # generate javascript plot and corresponding script tag
    js, tag = autoload_static(p, CDN, script_path + js_filename)

    with open(output_path + js_filename, 'w') as js_file:
        js_file.write(js)

    return tag

if __name__ == "__main__":
    print(plot())