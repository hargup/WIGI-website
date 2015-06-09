# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1433847981.576042
_enable_loop = True
_template_filename = u'/home/vivekrai/.miniconda/lib/python2.7/site-packages/nikola/data/themes/base/templates/index_helper.tmpl'
_template_uri = u'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['mathjax_script', 'html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if any(post.is_mathjax for post in posts):
            __M_writer(u'        <script type="text/x-mathjax-config">\n        MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});</script>\n        <script src="/assets/js/mathjax.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        prevlink = context.get('prevlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if prevlink or nextlink:
            __M_writer(u'        <nav class="postindexpager">\n        <ul class="pager">\n')
            if prevlink:
                __M_writer(u'            <li class="previous">\n                <a href="')
                __M_writer(unicode(prevlink))
                __M_writer(u'" rel="prev">')
                __M_writer(unicode(messages("Newer posts")))
                __M_writer(u'</a>\n            </li>\n')
            if nextlink:
                __M_writer(u'            <li class="next">\n                <a href="')
                __M_writer(unicode(nextlink))
                __M_writer(u'" rel="next">')
                __M_writer(unicode(messages("Older posts")))
                __M_writer(u'</a>\n            </li>\n')
            __M_writer(u'        </ul>\n        </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "20": 19, "21": 27, "27": 21, "32": 21, "33": 22, "34": 23, "40": 2, "47": 2, "48": 3, "49": 4, "50": 6, "51": 7, "52": 8, "53": 8, "54": 8, "55": 8, "56": 11, "57": 12, "58": 13, "59": 13, "60": 13, "61": 13, "62": 16, "68": 62}, "uri": "index_helper.tmpl", "filename": "/home/vivekrai/.miniconda/lib/python2.7/site-packages/nikola/data/themes/base/templates/index_helper.tmpl"}
__M_END_METADATA
"""
