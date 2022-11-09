from rest_framework.serializers import ModelSerializer

from one.cms.home.models import CMSHome


class CMSHomeSerializer(ModelSerializer):
    class Meta:
        model = CMSHome
        fields = "__all__"
