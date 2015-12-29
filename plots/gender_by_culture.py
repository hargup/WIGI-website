from __future__ import print_function

import pandas as pd
from bokeh._legacy_charts import Bar
from bokeh.models import NumeralTickFormatter

from .utils import write_plot, read_data


@write_plot('culture')
def plot(newest_changes):
    df, date_range = read_data(newest_changes, 'culture')

    # remove nan genders and nan rows
    del df['nan']
    df = df[list(map(lambda x: not pd.isnull(x), df.index))]

    df['total'] = df.sum(axis=1)
    df['nonbin'] = df['total'] - df['male'] - df['female']
    df['fem_per'] = df['female'] / (df['total'])
    df['nonbin_per'] = df['nonbin'] / df['total']
    df['fem_per_million'] = df['fem_per'] * 1000000
    df['nonbin_per_million'] = df['nonbin_per'] * 1000000
    dfs = df.sort_values('female')

    interesante = ['female', 'male', 'nonbin', 'total']

    p = Bar(dfs[['female', 'male']],
            stacked=True,
            xlabel="Culture",
            ylabel="Total gendered biographies",
            width=800,
            height=500,
            legend='top_left')

    p._yaxis.formatter = NumeralTickFormatter(format='0,0')
    htmltable = dfs[interesante].sort_values('female', ascending=False)
    htmltable.columns = ['Female', 'Male', 'Non Binary', 'Total']
    top_rows = htmltable.head(10).to_html(na_rep='n/a', classes=['table'])
    bottom_rows = htmltable[::-1].head(10).to_html(na_rep='n/a', classes=['table'])
    table_html = [top_rows, bottom_rows]

    return p, date_range, table_html

if __name__ == "__main__":
    print(plot('newest'))
    print(plot('newest-changes'))
