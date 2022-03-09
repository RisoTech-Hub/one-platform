from django.urls import path

from one.pages.views import page_update_view

app_name = "pages"
urlpatterns = [
    path("<str:pk>/", view=page_update_view, name="update"),
]
