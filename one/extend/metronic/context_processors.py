from django.conf import settings
from django.template import RequestContext

from one.extend.metronic.bootstrap.bootstrap import KTBootstrap
from one.extend.metronic.libs.theme import KTTheme


def layout_context(request):
    """Initial Metronic Layout context."""
    if dict(settings.__dict__).get("AUTH_URL", "accounts/") in request.path:
        return {}
    global_context = RequestContext(request)

    # Init the theme API
    KTTheme.init()

    # Init the base theme settings
    KTBootstrap.init()
    return {
        "layout": KTTheme.set_layout("default.html", global_context),  # noqa
    }
