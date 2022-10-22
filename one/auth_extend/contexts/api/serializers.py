from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer

from one.auth_extend.contexts.models import Context


class ContextSerializer(ModelSerializer):
    class Meta:
        model = Context
        fields = "__all__"


class GroupSerializer(ModelSerializer):
    context = ContextSerializer()

    class Meta:
        model = Group
        fields = ["id", "name", "context"]
