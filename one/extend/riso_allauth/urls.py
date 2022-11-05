from django.urls import path

from one.extend.riso_allauth.views import template_list_view, template_update_view

app_name = "allauth"
urlpatterns = [
    path("", view=template_list_view, name="template-list"),
    path("<str:pk>/", view=template_update_view, name="template-update"),
]
