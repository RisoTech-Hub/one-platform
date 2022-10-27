from django.conf import settings

from one.extend.metronic.libs.theme import KTTheme


class KTBootstrap:
    # Core global bootstrap class

    @staticmethod
    def init_theme_mode():
        # Init theme mode option from settings
        KTTheme.set_mode_switch(settings.KT_THEME_MODE_SWITCH_ENABLED)
        KTTheme.set_mode_default(settings.KT_THEME_MODE_DEFAULT)

    @staticmethod
    def init_theme_direction():
        # Init theme direction option (RTL or LTR) from settings
        # Init RTL html attributes by checking if RTL is enabled.
        # This function is being called for the html tag
        KTTheme.set_direction(settings.KT_THEME_DIRECTION)

        if KTTheme.is_rtl_direction():
            KTTheme.add_html_attribute("html", "direction", "rtl")
            KTTheme.add_html_attribute("html", "dir", "rtl")
            KTTheme.add_html_attribute("html", "style", "direction: rtl")

    @staticmethod
    def init_layout():
        # Init layout html attributes and classes
        KTTheme.add_html_attribute("body", "id", "kt_app_body")
        KTTheme.add_html_attribute("body", "data-kt-name", KTTheme.get_name())

    @staticmethod
    def init():
        # Main initialization
        KTBootstrap.init_theme_mode()
        KTBootstrap.init_theme_direction()
        KTBootstrap.init_layout()
