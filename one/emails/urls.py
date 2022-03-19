from django.urls import path

from one.emails.views import email_template_list_view

app_name = "emails"
urlpatterns = [
    path("", view=email_template_list_view, name="list"),
]
