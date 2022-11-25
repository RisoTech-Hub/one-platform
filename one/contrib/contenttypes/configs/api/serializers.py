from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import ModelSerializer

from one.contrib.contenttypes.configs.models import Config


class ConfigSerializer(ModelSerializer):
    class Meta:
        model = Config
        fields = "__all__"


class ContentTypeSerializer(ModelSerializer):
    config = ConfigSerializer()

    class Meta:
        model = ContentType
        fields = ["id", "app_label", "model", "config"]
