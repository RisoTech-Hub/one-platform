"""
This is an entry and Bootstrap class for the theme level.
The init() function will be called in _keenthemes/__init__.py
"""
from one.extend.metronic.libs.theme import KTTheme


class KTBootstrapSystem:
    @staticmethod
    def init(context):
        KTTheme.add_html_class("body", "app-blank")
        KTTheme.add_html_class(
            "body", "bgi-size-cover bgi-position-center bgi-no-repeat"
        )
