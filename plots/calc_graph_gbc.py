from __future__ import print_function
from bokeh.resources import CDN
from bokeh.plotting import figure, save, output_file
from bokeh.charts import Bar

# gbc => gender by culture
# Expecting 9 csv rows for with values each, first for number of female
# biographies and second for the total number of biographies


def load_data(data_path):
    import csv

    female = []
    total = []

    with open(data_path, 'r') as csvfile:

        gbcreader = csv.reader(csvfile)
        for row, culture in zip(gbcreader, cultures):
            f, t = row
            female.append(float(f))
            total.append(float(t))

    return {'female': female, 'total': total}


cultures = ['catholic europian',
            'african',
            'orthodox',
            'latin american',
            'islamic',
            'protestant european',
            'south asian', 'english speaking',
            'confucian']


data = load_data('./data/gender-by-culture.csv')
print(data)

output_file('bar.html')
plot = Bar(data, cat=cultures, title="gender by culture",
           xlabel='cultures', ylabel='% female', width=400, height=1000)


save(plot)
