from rest_framework.serializers import UUIDField

from one.components.serializers import LingualSerializer
from one.pages.models import Page


class PageSerializer(LingualSerializer):
    id = UUIDField(read_only=True)

    class Meta:
        model = Page
        fields = "__all__"
