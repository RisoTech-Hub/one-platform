from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from one.cms.home.api.views import CMSHomeViewSet
from one.core.menu.api.views import MenuViewSet
from one.extend.riso_allauth.api.views import TemplateViewSet
from one.extend.riso_auth.contexts.api.views import GroupViewSet
from one.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("cms/home", CMSHomeViewSet)
router.register("menu", MenuViewSet)
router.register("allauth", TemplateViewSet)
router.register("groups", GroupViewSet)
router.register("users", UserViewSet)

app_name = "api"
urlpatterns = router.urls
