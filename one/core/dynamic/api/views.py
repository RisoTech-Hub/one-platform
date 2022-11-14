from rest_framework.decorators import api_view
from rest_framework.response import Response

from one.components.viewsets import DeniedDeleteModelViewSet
from one.core.dynamic.api.serializers import FieldSchemaSerializer
from one.core.dynamic.constants import FIELD_TYPE_DEFAULT_ATTRS
from one.core.dynamic.models import FieldSchema


class FieldSchemaViewSet(DeniedDeleteModelViewSet):
    queryset = FieldSchema.objects.all()
    serializer_class = FieldSchemaSerializer


@api_view(["GET"])
def retrieve_attrs(request, attr_type=None):
    if attr_type:
        return Response(dict(FIELD_TYPE_DEFAULT_ATTRS)[attr_type], status=200)
    return Response(status=400)
