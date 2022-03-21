from one.components.viewsets import BaseModelViewSet
from one.pages.api.serializers import PageSerializer
from one.pages.models import Page


class PageViewSet(BaseModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
