from django.urls import path

from one.groups.views import group_detail_view, group_list_view, group_update_view

app_name = "groups"
urlpatterns = [
    path("", view=group_list_view, name="list"),
    path("~update/<str:id>/", view=group_update_view, name="update"),
    path("<str:id>/", view=group_detail_view, name="detail"),
]
