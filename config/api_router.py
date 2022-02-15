from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from one.users.api.views import ProfileViewSet, UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("profile", ProfileViewSet, basename="profile")
router.register("users", UserViewSet, basename="users")


app_name = "api"
urlpatterns = router.urls
