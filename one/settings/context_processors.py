from one.settings.models import Setting


def setting_settings(request):
    """Expose some application settings in templates."""
    setting = Setting.objects.filter(is_active=True).first()
    return {"MAIN_LOGO": setting.main_logo.url}
