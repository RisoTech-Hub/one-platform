from django.contrib.sites.models import Site
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from one.components.serializers import ExtraSerializer
from one.contrib.sites.settings.models import Setting


class SettingSerializer(ExtraSerializer, ModelSerializer):
    favicon = SerializerMethodField(method_name="favicon_serializer")

    class Meta:
        model = Setting
        fields = "__all__"

    def favicon_serializer(self, obj, *args, **kwargs):
        return super().image_serializer(obj, *args, field="favicon", **kwargs)


class SiteSerializer(ModelSerializer):
    setting = SettingSerializer()

    class Meta:
        model = Site
        fields = ["id", "name", "domain", "setting"]
