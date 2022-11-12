from rest_framework.serializers import ModelSerializer

from one.core.dynamic.models import Field, FieldSchema


class FieldSerializer(ModelSerializer):
    class Meta:
        model = Field
        fields = "__all__"


class FieldSchemaSerializer(ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = FieldSchema
        fields = ["id", "name", "fields"]
