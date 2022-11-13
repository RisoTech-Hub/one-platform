from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from filebrowser.sites import site
from rest_framework.authtoken.views import obtain_auth_token

third_urlpatterns = [
    # Notifications
    path("webpush/", include("webpush.urls")),
    # File Browser
    path("filebrowser/", site.urls),
    # TinyMCE
    path("tinymce/", include("tinymce.urls")),
]

cms_urlpatterns = [
    path("home/", include("one.cms.home.urls")),
]

urlpatterns = (
    third_urlpatterns
    + [
        path(
            "",
            login_required(TemplateView.as_view(template_name="pages/home.html")),
            name="home",
        ),
        path(
            "about/",
            TemplateView.as_view(template_name="pages/about.html"),
            name="about",
        ),
        # Django Admin, use {% url 'admin:index' %}
        path(settings.ADMIN_URL, admin.site.urls),
        # Django Language
        path("i18n/", include("django.conf.urls.i18n")),
        path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
        # Extend Packages
        path("~setting/", include("one.contrib.sites.settings.urls")),
        path("~group/", include("one.extend.riso_auth.contexts.urls")),
        path("~allauth/", include("one.extend.riso_allauth.urls")),
        path("~menu/", include("one.core.menu.urls")),
        path("~dynamic/schema/", include("one.core.dynamic.urls")),
        # CMS Management
        path("~cms/", include(cms_urlpatterns)),
        # User Management
        path("users/", include("one.users.urls", namespace="users")),
        path("accounts/", include("one.extend.riso_allauth.account.urls")),
        # Your stuff: custom urls includes go here
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
