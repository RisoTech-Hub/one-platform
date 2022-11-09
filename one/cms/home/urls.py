from django.urls import path

from one.cms.home.views import (
    cmshome_create_view,
    cmshome_list_view,
    cmshome_update_view,
)

app_name = "cmshome"
urlpatterns = [
    path("", view=cmshome_list_view, name="cmshome-list"),
    path("create", view=cmshome_create_view, name="cmshome-create"),
    path("<int:pk>/", view=cmshome_update_view, name="cmshome-update"),
]
