from django.urls import path

from one.settings.views import setting_list_view

app_name = "settings"
urlpatterns = [
    path("", view=setting_list_view, name="list"),
]
