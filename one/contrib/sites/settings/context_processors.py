from django.conf import settings
from django.contrib.sites.models import Site


def site_setting_processor(request):
    """Expose settings from site in templates."""
    return {
        "site": Site.objects.get_current(),
        "languages": settings.LANGUAGES,
        "default_language": settings.LANGUAGE_CODE.split("-")[0],
    }
