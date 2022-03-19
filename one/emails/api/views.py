from one.components.viewsets import BaseModelViewSet
from one.emails.api.serializers import EmailTemplateSerializer
from one.emails.models import EmailTemplate


class EmailTemplateViewSet(BaseModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer
