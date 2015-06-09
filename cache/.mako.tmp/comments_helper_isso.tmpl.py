# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1433847981.737426
_enable_loop = True
_template_filename = u'/home/vivekrai/.miniconda/lib/python2.7/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl'
_template_uri = u'comments_helper_isso.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system_id:
            __M_writer(u'        <div data-title="')
            __M_writer(filters.url_escape(unicode(title)))
            __M_writer(u'" id="isso-thread"></div>\n        <script src="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'js/embed.min.js" data-isso="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system_id:
            __M_writer(u'        <a href="')
            __M_writer(unicode(link))
            __M_writer(u'#isso-thread">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system_id:
            __M_writer(u'        <script src="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'js/count.min.js" data-isso="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "20": 7, "21": 13, "22": 20, "28": 2, "33": 2, "34": 3, "35": 4, "36": 4, "37": 4, "38": 5, "39": 5, "40": 5, "41": 5, "47": 9, "52": 9, "53": 10, "54": 11, "55": 11, "56": 11, "62": 16, "67": 16, "68": 17, "69": 18, "70": 18, "71": 18, "72": 18, "73": 18, "79": 73}, "uri": "comments_helper_isso.tmpl", "filename": "/home/vivekrai/.miniconda/lib/python2.7/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl"}
__M_END_METADATA
"""
