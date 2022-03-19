from rest_framework.viewsets import ModelViewSet

from one.emails.api.serializers import EmailTemplateSerializer
from one.emails.models import EmailTemplate


class EmailTemplateViewSet(ModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer
