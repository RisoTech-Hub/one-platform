from one.components.viewsets import DeniedDeleteModelViewSet
from one.core.dynamic.api.serializers import FieldSchemaSerializer
from one.core.dynamic.models import FieldSchema


class FieldSchemaViewSet(DeniedDeleteModelViewSet):
    queryset = FieldSchema.objects.all()
    serializer_class = FieldSchemaSerializer
