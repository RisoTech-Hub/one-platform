from django.urls import path

from one.core.menu.views import menu_create_view, menu_list_view, menu_update_view

app_name = "menu"
urlpatterns = [
    path("", view=menu_list_view, name="menu-list"),
    path("create/", view=menu_create_view, name="menu-create"),
    path("<str:pk>/", view=menu_update_view, name="menu-update"),
]
