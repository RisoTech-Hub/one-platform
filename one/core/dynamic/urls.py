from django.urls import path

from one.core.dynamic.views import field_schema_create_view, field_schema_update_view

app_name = "fieldschema"
urlpatterns = [
    path("create/", view=field_schema_create_view, name="fieldschema-create"),
    path("<str:pk>/", view=field_schema_update_view, name="fieldschema-update"),
]
