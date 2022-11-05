from rest_framework.serializers import ModelSerializer

from one.extend.riso_allauth.models import AllauthTemplate


class TemplateSerializer(ModelSerializer):
    class Meta:
        model = AllauthTemplate
        fields = ["id", "subject", "language"]
