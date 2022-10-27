from django import template
from django.utils.safestring import mark_safe

from one.extend.metronic.libs.theme import KTTheme

register = template.Library()


# Register tags as an adapter for the Theme class usage in the HTML template


@register.simple_tag(name="include_fonts")
def do_include_fonts():
    return mark_safe(KTTheme.include_fonts())


@register.simple_tag(name="include_favicon")
def do_include_favicon():
    return mark_safe(KTTheme.include_favicon())


@register.simple_tag(name="get_svg_icon")
def do_get_svg_icon(path, class_names="svg-icon", folder="media/icons/"):
    return mark_safe(KTTheme.get_svg_icon(path, class_names, folder))


@register.simple_tag(name="print_html_classes")
def do_print_html_classes(scope):
    return mark_safe(KTTheme.print_html_classes(scope))


@register.simple_tag(name="print_html_attributes")
def do_print_html_attributes(scope):
    return mark_safe(KTTheme.print_html_attributes(scope))


@register.simple_tag(name="get_global_assets")
def do_get_global_assets(asset_type):
    return KTTheme.get_global_assets(asset_type)


@register.simple_tag(name="get_custom_js")
def do_get_custom_js():
    return KTTheme.javascript_files


@register.simple_tag(name="get_custom_css")
def do_get_custom_css():
    return KTTheme.css_files


@register.simple_tag(name="get_vendors")
def do_get_vendors(vendor_type):
    return KTTheme.get_vendors(vendor_type)


@register.simple_tag(name="is_rtl_direction")
def do_is_rtl_direction():
    return KTTheme.is_rtl_direction()


@register.simple_tag(name="asset")
def do_asset(path):
    return KTTheme.asset(path)


@register.simple_tag(name="get_mode_default")
def do_get_mode_default():
    return KTTheme.get_mode_default()


@register.simple_tag(name="add_html_attribute")
def do_add_html_attribute(scope, name, value):
    KTTheme.add_html_attribute(scope, name, value)
    return ""


@register.simple_tag(name="add_html_class")
def do_add_html_attributes(scope, attributes):
    KTTheme.add_html_attributes(scope, attributes)
    return ""


@register.simple_tag(name="add_html_class")
def do_add_html_class(scope, value):
    KTTheme.add_html_class(scope, value)
    return ""


@register.simple_tag(name="get_html_classes")
def do_get_html_attribute(scope, attribute):
    return KTTheme.html_attributes[scope][attribute]
