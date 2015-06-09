# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1433847981.606546
_enable_loop = True
_template_filename = u'/home/vivekrai/.miniconda/lib/python2.7/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl'
_template_uri = u'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'livefyre', context._clean_inheritance_tokens(), templateuri=u'comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'livefyre')] = ns

    ns = runtime.TemplateNamespace(u'googleplus', context._clean_inheritance_tokens(), templateuri=u'comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'googleplus')] = ns

    ns = runtime.TemplateNamespace(u'facebook', context._clean_inheritance_tokens(), templateuri=u'comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'facebook')] = ns

    ns = runtime.TemplateNamespace(u'muut', context._clean_inheritance_tokens(), templateuri=u'comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'muut')] = ns

    ns = runtime.TemplateNamespace(u'disqus', context._clean_inheritance_tokens(), templateuri=u'comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'disqus')] = ns

    ns = runtime.TemplateNamespace(u'intensedebate', context._clean_inheritance_tokens(), templateuri=u'comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'intensedebate')] = ns

    ns = runtime.TemplateNamespace(u'isso', context._clean_inheritance_tokens(), templateuri=u'comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'isso')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        isso = _mako_get_namespace(context, 'isso')
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system == 'disqus':
            __M_writer(u'        ')
            __M_writer(unicode(disqus.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'livefyre':
            __M_writer(u'        ')
            __M_writer(unicode(livefyre.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'intensedebate':
            __M_writer(u'        ')
            __M_writer(unicode(intensedebate.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'muut':
            __M_writer(u'        ')
            __M_writer(unicode(muut.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'googleplus':
            __M_writer(u'        ')
            __M_writer(unicode(googleplus.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'facebook':
            __M_writer(u'        ')
            __M_writer(unicode(facebook.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'isso':
            __M_writer(u'        ')
            __M_writer(unicode(isso.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        isso = _mako_get_namespace(context, 'isso')
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system == 'disqus':
            __M_writer(u'        ')
            __M_writer(unicode(disqus.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'livefyre':
            __M_writer(u'        ')
            __M_writer(unicode(livefyre.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'intensedebate':
            __M_writer(u'        ')
            __M_writer(unicode(intensedebate.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'muut':
            __M_writer(u'        ')
            __M_writer(unicode(muut.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'googleplus':
            __M_writer(u'        ')
            __M_writer(unicode(googleplus.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'facebook':
            __M_writer(u'        ')
            __M_writer(unicode(facebook.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'isso':
            __M_writer(u'        ')
            __M_writer(unicode(isso.comment_link(link, identifier)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        facebook = _mako_get_namespace(context, 'facebook')
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        isso = _mako_get_namespace(context, 'isso')
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system == 'disqus':
            __M_writer(u'        ')
            __M_writer(unicode(disqus.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'livefyre':
            __M_writer(u'        ')
            __M_writer(unicode(livefyre.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'intensedebate':
            __M_writer(u'        ')
            __M_writer(unicode(intensedebate.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'muut':
            __M_writer(u'        ')
            __M_writer(unicode(muut.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'googleplus':
            __M_writer(u'        ')
            __M_writer(unicode(googleplus.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'facebook':
            __M_writer(u'        ')
            __M_writer(unicode(facebook.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'isso':
            __M_writer(u'        ')
            __M_writer(unicode(isso.comment_link_script()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 4, "25": 7, "28": 8, "31": 6, "34": 3, "37": 5, "40": 9, "43": 0, "48": 2, "49": 3, "50": 4, "51": 5, "52": 6, "53": 7, "54": 8, "55": 9, "56": 27, "57": 45, "58": 63, "64": 11, "76": 11, "77": 12, "78": 13, "79": 13, "80": 13, "81": 14, "82": 15, "83": 15, "84": 15, "85": 16, "86": 17, "87": 17, "88": 17, "89": 18, "90": 19, "91": 19, "92": 19, "93": 20, "94": 21, "95": 21, "96": 21, "97": 22, "98": 23, "99": 23, "100": 23, "101": 24, "102": 25, "103": 25, "104": 25, "110": 29, "122": 29, "123": 30, "124": 31, "125": 31, "126": 31, "127": 32, "128": 33, "129": 33, "130": 33, "131": 34, "132": 35, "133": 35, "134": 35, "135": 36, "136": 37, "137": 37, "138": 37, "139": 38, "140": 39, "141": 39, "142": 39, "143": 40, "144": 41, "145": 41, "146": 41, "147": 42, "148": 43, "149": 43, "150": 43, "156": 47, "168": 47, "169": 48, "170": 49, "171": 49, "172": 49, "173": 50, "174": 51, "175": 51, "176": 51, "177": 52, "178": 53, "179": 53, "180": 53, "181": 54, "182": 55, "183": 55, "184": 55, "185": 56, "186": 57, "187": 57, "188": 57, "189": 58, "190": 59, "191": 59, "192": 59, "193": 60, "194": 61, "195": 61, "196": 61, "202": 196}, "uri": "comments_helper.tmpl", "filename": "/home/vivekrai/.miniconda/lib/python2.7/site-packages/nikola/data/themes/base/templates/comments_helper.tmpl"}
__M_END_METADATA
"""
