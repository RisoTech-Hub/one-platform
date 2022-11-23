from django.contrib.sites.models import Site

from one.components.viewsets import BaseModelViewSet
from one.contrib.sites.settings.api.serializers import SiteSerializer


class SiteViewSet(BaseModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
