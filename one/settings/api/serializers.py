from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import SerializerMethodField, UUIDField

from one.components.serializers import BaseSerializer
from one.settings.models import Setting


class SettingSerializer(BaseSerializer):
    id = UUIDField(read_only=True)
    main_logo = SerializerMethodField()
    is_active = SerializerMethodField()

    class Meta:
        model = Setting
        fields = "__all__"

    @staticmethod
    def get_main_logo(obj):
        return f"<img src='{obj.main_logo.url}'>"

    @staticmethod
    def get_is_active(obj):
        return (
            f"<span class='badge badge-success'>{_('Active')}</span>"
            if obj.is_active
            else f"<span class='badge badge-danger'>{_('Not Active')}</span>"
        )
