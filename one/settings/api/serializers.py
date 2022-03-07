from rest_framework.serializers import ModelSerializer, SerializerMethodField, UUIDField

from one.settings.models import Setting


class SettingSerializer(ModelSerializer):
    id = UUIDField(read_only=True)
    main_logo = SerializerMethodField()

    class Meta:
        model = Setting
        fields = "__all__"

    def get_main_logo(self, obj):
        return f"<img src='{obj.main_logo.url}'>"
