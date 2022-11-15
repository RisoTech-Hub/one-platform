from one.components.viewsets import BaseModelViewSet
from one.extend.riso_allauth.api.serializers import TemplateSerializer
from one.extend.riso_allauth.models import AllauthTemplate


class TemplateViewSet(BaseModelViewSet):
    queryset = AllauthTemplate.objects.all()
    serializer_class = TemplateSerializer
    actions = ["change"]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
