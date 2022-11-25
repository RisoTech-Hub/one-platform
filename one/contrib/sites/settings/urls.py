from django.urls import path

from one.contrib.sites.settings.views import site_update_view

app_name = "sites"
urlpatterns = [path("", view=site_update_view, name="site-update")]
