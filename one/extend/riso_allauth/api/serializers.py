from rest_framework.serializers import ModelSerializer, SerializerMethodField

from one.extend.riso_allauth.models import AllauthTemplate


class TemplateSerializer(ModelSerializer):
    code = SerializerMethodField()

    class Meta:
        model = AllauthTemplate
        fields = ["id", "subject", "code"]

    def get_code(self, obj):  # noqa
        return obj.code_verbose
