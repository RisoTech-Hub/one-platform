from rest_framework.serializers import SerializerMethodField, UUIDField

from one.components.serializers import BaseSerializer
from one.settings.models import Setting


class SettingSerializer(BaseSerializer):
    id = UUIDField(read_only=True)
    main_logo = SerializerMethodField()

    class Meta:
        model = Setting
        fields = "__all__"

    def get_main_logo(self, obj):
        return f"<img src='{obj.main_logo.url}'>"
