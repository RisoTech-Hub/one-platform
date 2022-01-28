def applications_settings(request):
    """Expose some application settings in templates."""
    applications = {
        "ENABLE_LIVE_CHAT_APPLICATION": False,
        "ENABLE_ACTIVITIES": False,
        "ENABLE_NOTIFICATION": False,
        "ENABLE_QUICK_LINKS": False,
    }
    return applications
