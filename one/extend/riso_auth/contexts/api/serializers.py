from django.contrib.auth.models import Group
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from one.components.serializers import ExtraSerializer
from one.extend.riso_auth.contexts.models import Context


class ContextSerializer(ExtraSerializer, ModelSerializer):
    avatar = SerializerMethodField(method_name="image_serializer")

    class Meta:
        model = Context
        fields = "__all__"

    def image_serializer(self, obj, *args, **kwargs):
        return super().image_serializer(obj, *args, field="avatar", **kwargs)


class GroupSerializer(ModelSerializer):
    context = ContextSerializer()

    class Meta:
        model = Group
        fields = ["id", "name", "context"]
