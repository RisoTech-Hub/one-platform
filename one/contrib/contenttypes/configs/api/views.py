from django.contrib.contenttypes.models import ContentType

from one.components.viewsets import BaseModelViewSet
from one.contrib.contenttypes.configs.api.serializers import ContentTypeSerializer


class ContentTypeViewSet(BaseModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
