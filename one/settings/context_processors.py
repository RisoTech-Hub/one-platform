from django.core.cache import cache

from one.settings.models import Setting


def setting_settings(request):
    """Expose some application settings in templates."""
    setting = cache.get("ACTIVE_SETTING")
    if not setting:
        setting = Setting.objects.filter(is_active=True).first()
        cache.set("ACTIVE_SETTING", setting, None)
    return {"MAIN_LOGO": setting.main_logo.url}
