from rest_framework.serializers import ModelSerializer, SerializerMethodField

from one.extend.riso_allauth.models import AllauthTemplate


class TemplateSerializer(ModelSerializer):
    language = SerializerMethodField()

    class Meta:
        model = AllauthTemplate
        fields = ["id", "subject", "language"]

    def get_language(self, obj):  # noqa
        return obj.get_language_display()
