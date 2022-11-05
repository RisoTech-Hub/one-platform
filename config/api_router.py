from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from one.extend.riso_allauth.api.views import TemplateViewSet
from one.extend.riso_auth.contexts.api.views import GroupViewSet
from one.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
router.register("allauth", TemplateViewSet)

app_name = "api"
urlpatterns = router.urls
