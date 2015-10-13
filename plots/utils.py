from __future__ import print_function
from bokeh.resources import CDN
from bokeh.embed import autoload_static
import os
import pandas
from dateutil.parser import parse


def get_date_range(start, end):
    start = parse(start)
    end = parse(end)
    print(start)
    print(end)
    return "{} - {}".format(start.strftime("%d %b '%y"),
            end.strftime("%d %b '%y"))


def plot_wrapper(plot_func, newest_changes):
    # XXX: the characteristic for gender_by_country plot is not consistent, the
    # data files starts with worldfiles instead of country, that needs to be
    # changed.
    characteristic = plot_func.__name__.split('_')[-1]

    filelist = os.listdir('/home/maximilianklein/snapshot_data/{}/'.format(newest_changes))
    characteristic_file = [f for f in filelist if f.startswith(characteristic)][0]
    if newest_changes == 'newest-changes':
        date_range = characteristic_file.split('{}-index-from-'.format(characteristic))[1].split('.csv')[0].replace('-',' ')
        print(date_range)
    csv_to_read = '/home/maximilianklein/snapshot_data/{}/{}'.format(newest_changes, characteristic_file)
    df = pandas.DataFrame.from_csv(csv_to_read)

    p, table_html = plot_func(df, date_range, newest_changes)

    js_filename = "gender_by_{}_{}.js".format(characteristic, newest_changes)
    script_path = "./assets/js/"
    output_path = "./files/assets/js/"

    js, tag = autoload_static(p, CDN, script_path + js_filename)

    with open(output_path + js_filename, 'w') as js_file:
        js_file.write(js)

    return {'plot_tag': tag, 'table_html': table_html}
