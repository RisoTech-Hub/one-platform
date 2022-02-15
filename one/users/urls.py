from django.urls import path

from one.users.views import (
    profile_detail_view,
    profile_update_view,
    user_detail_view,
    user_list_view,
    user_redirect_view,
)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=profile_update_view, name="update"),
    path("<str:username>/", view=profile_detail_view, name="detail"),
    path("<str:username>/view/", view=user_detail_view, name="view"),
]
