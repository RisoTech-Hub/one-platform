from django.urls import path

from one.pages.views import page_list_view, page_update_view

app_name = "pages"
urlpatterns = [
    path("", view=page_list_view, name="list"),
    path("<str:pk>/", view=page_update_view, name="update"),
]
