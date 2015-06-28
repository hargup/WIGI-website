import pandas
from bokeh.charts import TimeSeries
from bokeh.plotting import gridplot
from bokeh.resources import CDN
from bokeh.embed import autoload_static
import dateutil


def create_gender_by_dob_plot():
    ra_len = 1

    dox = pandas.DataFrame()
    nonbindox = pandas.DataFrame()

    for l in ['b', 'd']:
        acro = 'do'+l
        df = pandas.DataFrame.from_csv('./data/%s-index.csv' % acro)
        del df['nan']
        df['total'] = df.sum(axis=1)
        df['nonbin'] = df['total'] - df['male'] - df['female']
        df['fem_per'] = df['female'] / (df['total'])
        df['nonbin_per'] = df['nonbin'] / df['total']

        ra = pandas.rolling_mean(df['fem_per'], ra_len)
        dox[acro] = ra

        nonbinra = pandas.rolling_mean(df['nonbin_per'], ra_len)
        nonbindox[acro] = nonbinra

    time_range = (1400, 2014)

    dox = dox[time_range[0]: time_range[1]]
    dox['Date'] = [dateutil.parser.parse(str(int(x)))
                   for x in dox['dob'].keys()]

    p1 = TimeSeries(dox, index='Date', legend=True, title="Female Ratios")
    p1.below[0].formatter.formats = dict(years=['%Y'])


    nonbindox = nonbindox[time_range[0]: time_range[1]]
    nonbindox['Date'] = [dateutil.parser.parse(str(int(x)))
                         for x in nonbindox['dob'].keys()]

    p2 = TimeSeries(nonbindox, index='Date', legend=True, title="Non Binary Ratios")
    p2.below[0].formatter.formats = dict(years=['%Y'])

    p = gridplot([[p1], [p2]], toolbar_location=None)

    js_file_name = "gender_by_country.js"
    script_path = "./scripts/"
    output_path = "output/scripts/"
    js, tag = autoload_static(p, CDN, script_path + js_file_name)

    with open(output_path + js_file_name, 'w') as js_file:
        js_file.write(js)

    return tag


if __name__ == "__main__":
    print(create_gender_by_dob_plot())

# fig, (pltf, pltb) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(9, 6))
# dox.plot(kind='line',  cmap='Paired', linewidth=2, ax=pltf)
# pltf.set_xlim((1400, 2014))
# pltf.set_ylim((0, 0.7))
# pltf.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, y: '{}%'.format(int(x*100))))
# pltf.set_title('Female ratio')
# pltf.legend(('Date of Birth', 'Date of Death'), loc=4, bbox_to_anchor=(1.25, -0.25))
#
# nonbindox.plot(kind='line',  cmap='Paired', linewidth=2, ax=pltb, legend=False)
# pltb.set_xlim((1400, 2014))
# pltb.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, y: '{}%'.format(x*100)))
# pltb.set_title('Non-binary Ratio')
#
# fig.suptitle('Composition of Wikidata Genders in Modern History', fontsize=24)
# fig.subplots_adjust(top=0.87)
#
# plt.savefig('./output/plots/gender_by_dob.png')
