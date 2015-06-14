import pandas
import matplotlib.pyplot as plt
import matplotlib


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


fig, (pltf, pltb) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(9, 6))
dox.plot(kind='line',  cmap='Paired', linewidth=2, ax=pltf)
pltf.set_xlim((1400, 2014))
pltf.set_ylim((0, 0.7))
pltf.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, y: '{}%'.format(int(x*100))))
pltf.set_title('Female ratio')
pltf.legend(('Date of Birth', 'Date of Death'), loc=4, bbox_to_anchor=(1.25, -0.25))

nonbindox.plot(kind='line',  cmap='Paired', linewidth=2, ax=pltb, legend=False)
pltb.set_xlim((1400, 2014))
pltb.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, y: '{}%'.format(x*100)))
pltb.set_title('Non-binary Ratio')

fig.suptitle('Composition of Wikidata Genders in Modern History', fontsize=24)
fig.subplots_adjust(top=0.87)

plt.savefig('./output/plots/gender_by_dob.png')
