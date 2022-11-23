from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from one.cms.home.api.views import CMSHomeViewSet
from one.contrib.sites.settings.api.views import SiteViewSet
from one.core.dynamic.api.views import FieldSchemaViewSet, retrieve_attrs
from one.core.menu.api.views import MenuViewSet
from one.extend.riso_allauth.api.views import TemplateViewSet
from one.extend.riso_auth.contexts.api.views import GroupViewSet
from one.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# CORE
router.register("core/menu", MenuViewSet)
router.register("core/field-schema", FieldSchemaViewSet)

# CMS
router.register("cms/home", CMSHomeViewSet)

# APPS
router.register("allauth", TemplateViewSet)
router.register("sites", SiteViewSet)
router.register("groups", GroupViewSet)
router.register("users", UserViewSet)

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path(
        "core/field-schema/retrieve-attrs/<str:attr_type>",
        retrieve_attrs,
        name="retrieve-attrs",
    ),
]
