from one.extend.metronic.bootstrap.bootstrap import KTBootstrap
from one.extend.metronic.libs.theme import KTTheme


class KTLayout:

    # Initialize the bootstrap files and page layout
    @staticmethod
    def init(context):
        # Init the theme API
        KTTheme.init()

        # Set a default layout globally. Can be set in the page level view file as well.
        # See example in dashboards/views.py
        context.update(
            {
                "layout": KTTheme.set_layout("default.html", context),
            }
        )

        # Init the base theme settings
        KTBootstrap.init()

        # Return context
        return context
