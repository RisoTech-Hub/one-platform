from rest_framework.serializers import ModelSerializer, UUIDField

from one.settings.models import Setting


class SettingSerializer(ModelSerializer):
    id = UUIDField(read_only=True)

    class Meta:
        model = Setting
        fields = "__all__"
