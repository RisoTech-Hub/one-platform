from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from one.users.api.views import ProfileViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", ProfileViewSet)


app_name = "api"
urlpatterns = router.urls
