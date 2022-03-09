from rest_framework.viewsets import ModelViewSet

from one.pages.api.serializers import PageSerializer
from one.pages.models import Page


class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
