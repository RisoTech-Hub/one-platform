from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from one.auth_extend.contexts.api.serializers import GroupSerializer
from one.components.viewsets import BaseModelViewSet


class GroupViewSet(BaseModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_fields = [
        {
            "key": "group",
            "label": _("Group"),
            "data_label": "name",
            "data_value": "pk",
            "model": Group,
        }
    ]
