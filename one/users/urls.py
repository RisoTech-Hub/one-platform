from django.urls import path

from one.users.views import profile_detail_view, profile_update_view, user_redirect_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=profile_update_view, name="update"),
    path("~profile/<str:username>/", view=profile_detail_view, name="detail"),
]
