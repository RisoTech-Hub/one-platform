from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import SerializerMethodField, UUIDField

from one.components.serializers import LingualSerializer
from one.emails.models import EmailTemplate


class EmailTemplateSerializer(LingualSerializer):
    id = UUIDField(read_only=True)
    is_protected = SerializerMethodField()

    class Meta:
        model = EmailTemplate
        fields = "__all__"

    @staticmethod
    def get_is_protected(obj):
        return (
            f"<span class='badge badge-success'>{_('Protected')}</span>"
            if obj.is_protected
            else f"<span class='badge badge-danger'>{_('Not Protect')}</span>"
        )
