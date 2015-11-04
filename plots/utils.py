from __future__ import print_function
from bokeh.resources import CDN
from bokeh.embed import autoload_static
from dateutil.parser import parse


def get_date_range(start, end):
    start = parse(start)
    end = parse(end)
    print(start)
    print(end)
    return "{} - {}".format(start.strftime("%d %b '%y"),
                            end.strftime("%d %b '%y"))


def write_plot(plot_func):
    def ret_func(newest_changes):
        characteristic = plot_func.__name__.split('_')[-1]

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

    return ret_func
