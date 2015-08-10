from __future__ import print_function
import pandas
from bokeh.charts import Bar, output_notebook, show
from bokeh.plotting import figure
from bokeh.models import NumeralTickFormatter
from bokeh.resources import CDN
from bokeh.embed import autoload_static
from bokeh.models import LinearAxis, Range1d


def plot():
    df = pandas.DataFrame.from_csv('/home/maximilianklein/snapshot_data/newest/culture-index.csv')
    no_gender_perc = df['nan'].sum() / df.sum().sum()
    del df['nan']
    df['total'] = df.sum(axis=1)
    df['nonbin'] = df['total'] - df['male'] - df['female']
    df['fem_per'] = df['female'] / (df['total'])
    df['nonbin_per'] = df['nonbin'] / df['total']
    df['fem_per_million'] = df['fem_per'] * 1000000
    df['nonbin_per_million'] = df['nonbin_per'] * 1000000

    dfs = df.sort('total')
    p = Bar(dfs[['total','fem_per_million','nonbin_per_million']], title="Gender By Inglehart-Welzel Culture",
              xlabel = "Culture",
              ylabel = "Total gendered biographies (Red), Female Percentage *1,000,00(Green)")
    #bar.yaxis.formatter = NumeralTickFormatter(format="0.0%")

    js_filename = "gender_by_culture.js"
    output_path = "./files/assets/js/"
    script_path = "./assets/js/"

    # generate javascript plot and corresponding script tag
    js, tag = autoload_static(p, CDN, script_path + js_filename)

    with open(output_path + js_filename, 'w') as js_file:
        js_file.write(js)

    return tag

if __name__ == "__main__":
    print(plot())

