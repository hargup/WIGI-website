from __future__ import print_function
import pandas
from bokeh.charts import Bar, output_notebook, show
from bokeh.plotting import figure
from bokeh.models import NumeralTickFormatter
from bokeh.resources import CDN
from bokeh.embed import autoload_static
from bokeh.models import LinearAxis, Range1d
import os


def plot(newest_changes):
    filelist = os.listdir('/home/maximilianklein/snapshot_data/{}/'.format(newest_changes))
    culture_file = [f for f in filelist if f.startswith('culture')][0]
    if newest_changes == 'newest-changes':
        date_range = culture_file.split('culture-index-from-')[1].split('.csv')[0].replace('-',' ')
        print(date_range)
    csv_to_read = '/home/maximilianklein/snapshot_data/{}/{}'.format(newest_changes,culture_file)

    df = pandas.DataFrame.from_csv(csv_to_read)
    no_gender_perc = df['nan'].sum() / df.sum().sum()
    del df['nan']
    df['total'] = df.sum(axis=1)
    df['nonbin'] = df['total'] - df['male'] - df['female']
    df['fem_per'] = df['female'] / (df['total'])
    df['nonbin_per'] = df['nonbin'] / df['total']
    df['fem_per_million'] = df['fem_per'] * 1000000
    df['nonbin_per_million'] = df['nonbin_per'] * 1000000
    dfs = df.sort('female')
    
    interesante = ['female','male','nonbin']
    htmltable = dfs[interesante]
    htmltable.columns=['Women','Men', 'Non-binary']
    table_html = htmltable.to_html(na_rep='n/a')

    title_suffix = 'Changes since {}'.format(date_range) if newest_changes == 'newest-changes' else 'All Time'

    p = Bar(dfs[interesante], title="Gender By Inglehart-Welzel Culture {}".format(title_suffix),
              xlabel = "Culture",
              ylabel = "Total gendered biographies (Red), Female Percentage *1,000,00(Green)")
    #bar.yaxis.formatter = NumeralTickFormatter(format="0.0%")

    js_filename = "gender_by_culture_{}.js".format(newest_changes)
    output_path = "./files/assets/js/"
    script_path = "./assets/js/"

    # generate javascript plot and corresponding script tag
    js, tag = autoload_static(p, CDN, script_path + js_filename)

    with open(output_path + js_filename, 'w') as js_file:
        js_file.write(js)

    return {'plot_tag':tag, 'table_html':table_html}

if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
