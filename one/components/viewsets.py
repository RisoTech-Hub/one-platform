from django.core.exceptions import FieldError
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from one.utils.data_processing import getattr_in_chain


class BaseModelViewSet(ModelViewSet):
    """
    Custom ModelViewSet
    """

    actions = None
    filter_fields = []

    def get_options(self):
        return "options", [
            {
                "key": item["key"],
                "label": item["label"],
                "data": [
                    {
                        "label": getattr_in_chain(obj, item["data_label"]),
                        "value": getattr_in_chain(obj, item["data_value"]),
                    }
                    for obj in item["model"].objects.all()
                ],
            }
            for item in self.filter_fields
        ]

    def get_labels(self):  # noqa
        return "labels", {
            "confirm_delete": _("Are you sure you want to delete selected records?"),
            "delete_success": _("Deleted Completely"),
            "delete_fail": _("This record was not deleted."),
            "confirm_btn_delete": _("Yes, delete!"),
            "cancel_btn_delete": _("No, cancel"),
            "notification_success_delete": _("You have deleted all selected records!."),
            "notification_confirm_button": _("Ok, got it!"),
            "notification_error_title": _("Notice"),
            "notification_error_text": _("Something is error:"),
            "action_col_title": _("Actions"),
            "edit_row": _("Update Item"),
            "view_row": _("View Item"),
            "error": _("Error"),
            "success": _("Success"),
        }

    def get_action_list(self):  # noqa
        return "action_list", ["add", "change", "delete", "view"]

    def get_actions(self):  # noqa
        if self.actions is not None:
            return "actions", self.actions
        return "actions", ["change", "delete"]

    class Meta:
        datatables_extra_json = ("get_labels", "get_actions", "get_action_list")

    def get_model(self):
        """return model of class"""
        return self.serializer_class.Meta.model

    @action(detail=False, methods=["delete"])
    def delete(self, request, *args, **kwargs):
        instances = self.queryset.filter(pk__in=request.data)
        try:
            instances = instances.filter(is_protected=False)
        except FieldError:
            pass
        instances.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class DeniedDeleteModelViewSet(BaseModelViewSet):
    @action(detail=False, methods=["delete"])
    def delete(self, request, *args, **kwargs):
        return Response(status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response(status=HTTP_400_BAD_REQUEST)
