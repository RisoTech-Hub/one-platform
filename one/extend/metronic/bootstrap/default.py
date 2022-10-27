"""
This is an entry and Bootstrap class for the theme level.
The init() function will be called in _keenthemes/__init__.py
"""
from one.extend.metronic.libs.theme import KTTheme


class KTBootstrapDefault:
    @staticmethod
    def init(context):
        # Init default layout

        """
        See also file starterkit/_keenthemes/__init__.py
        Below layout function need to included with the particular HTML layout file.
        """
        # 1) Light sidebar layout (default.html)
        # KTBootstrapDefault.init_light_sidebar_layout(context)

        # 2) Dark sidebar layout (default.html)
        KTBootstrapDefault.init_dark_sidebar_layout(context)

        # 3) Dark header layout (default_header_layout.html)
        # KTBootstrapDefault.init_dark_header_layout(context)

        # 4) Light header layout (default_header_layout.html)
        # KTBootstrapDefault.init_light_header_layout(context)

        # Init global assets for default layout
        KTBootstrapDefault.init_assets(context)

        return context

    @staticmethod
    def init_assets(context):
        # Include global vendors
        KTTheme.add_vendors(["datatables", "fullcalendar"])

        # Include global javascript files
        KTTheme.add_javascript_file("js/widgets.bundle.js")
        KTTheme.add_javascript_file("js/custom/apps/chat/chat.js")
        KTTheme.add_javascript_file("js/custom/utilities/modals/upgrade-plan.js")
        KTTheme.add_javascript_file("js/custom/utilities/modals/create-app.js")
        KTTheme.add_javascript_file("js/custom/utilities/modals/users-search.js")
        KTTheme.add_javascript_file("js/custom/utilities/modals/new-target.js")

        return context

    @staticmethod
    def init_dark_sidebar_layout(context):
        KTTheme.add_html_attribute("body", "data-kt-app-layout", "dark-sidebar")
        KTTheme.add_html_attribute("body", "data-kt-app-header-fixed", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-enabled", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-fixed", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-hoverable", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-push-header", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-push-toolbar", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-push-footer", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-toolbar-enabled", "true")

        KTTheme.add_html_class("body", "app-default")

        return context

    @staticmethod
    def init_light_sidebar_layout(context):
        KTTheme.add_html_attribute("body", "data-kt-app-layout", "light-sidebar")
        KTTheme.add_html_attribute("body", "data-kt-app-header-fixed", "false")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-enabled", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-fixed", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-hoverable", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-push-header", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-push-toolbar", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-sidebar-push-footer", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-toolbar-enabled", "true")

        KTTheme.add_html_class("body", "app-default")

        return context

    @staticmethod
    def init_dark_header_layout(context):
        KTTheme.add_html_attribute("body", "data-kt-app-layout", "dark-header")
        KTTheme.add_html_attribute("body", "data-kt-app-header-fixed", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-toolbar-enabled", "true")

        KTTheme.add_html_class("body", "app-default")

        return context

    @staticmethod
    def init_light_header_layout(context):
        KTTheme.add_html_attribute("body", "data-kt-app-layout", "light-header")
        KTTheme.add_html_attribute("body", "data-kt-app-header-fixed", "true")
        KTTheme.add_html_attribute("body", "data-kt-app-toolbar-enabled", "true")

        KTTheme.add_html_class("body", "app-default")

        return context
