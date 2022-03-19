from rest_framework.serializers import UUIDField

from one.components.serializers import BaseSerializer
from one.emails.models import EmailTemplate


class EmailTemplateSerializer(BaseSerializer):
    id = UUIDField(read_only=True)

    class Meta:
        model = EmailTemplate
        fields = "__all__"
