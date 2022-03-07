def applications_settings(request):
    """Expose some application settings in templates."""
    applications = {
        "ENABLE_LIVE_CHAT_APPLICATION": False,
        "ENABLE_ACTIVITIES": False,
        "ENABLE_NOTIFICATION": False,
        "ENABLE_QUICK_LINKS": False,
    }
    return applications


def menu_settings(request):
    """Base Menu config"""
    menus = {
        "ENABLE_MENU_SETTINGS": True,
        "ENABLE_MENU_EMAIL_TEMPLATE": False,
        "ENABLE_MENU_USER_MANAGEMENT": False,
        "ENABLE_MENU_PAGES": True,
    }
    return menus
