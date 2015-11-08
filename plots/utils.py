from __future__ import print_function
import os
from dateutil.parser import parse

import pandas as pd
from bokeh.resources import CDN
from bokeh.embed import autoload_static

from .config import data_dir


def get_date_range(start, end):
    start = parse(start)
    end = parse(end)
    print(start)
    print(end)
    return "{} - {}".format(start.strftime("%d %b '%y"),
                            end.strftime("%d %b '%y"))


def write_plot(characteristic):
    def write_plot_decorator(plot_func):
        def wrapped_func(newest_changes):
            p, date_range, table_html = plot_func(newest_changes)

            js_filename = "gender_by_{}_{}.js".format(characteristic,
                                                      newest_changes)
            script_path = "./assets/js/"
            output_path = "./files/assets/js/"

            js, tag = autoload_static(p, CDN, script_path + js_filename)

            with open(output_path + js_filename, 'w') as js_file:
                js_file.write(js)

            return {'plot_tag': tag,
                    'table_html': table_html,
                    'date_range': date_range}

        return wrapped_func
    return write_plot_decorator


def read_data(type_data, prefix):
    """
    type_data: Can be 'newest' or 'newest-changes'.
    prefix:
    """
    # XXX: Find better names for parameters
    filelist = os.listdir('{}/{}/'.format(data_dir, type_data))
    site_linkss_file = [f for f in filelist if f.startswith(prefix)][0]
    date_range = ""
    if type_data == 'newest-changes':
        start, end = site_linkss_file.split('{}-index-from-'.format(prefix))[1].split('.csv')[0].split('-to-')
        date_range = get_date_range(start, end)
        print(date_range)
    csv_to_read = '{}/{}/{}'.format(data_dir, type_data, site_linkss_file)
    df = pd.DataFrame.from_csv(csv_to_read)
    return df, date_range
