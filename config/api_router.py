from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from one.settings.api.views import SettingViewSet
from one.users.api.views import ProfileViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("profile", ProfileViewSet, basename="profile")
router.register("settings", SettingViewSet, basename="settings")

app_name = "api"
urlpatterns = router.urls
