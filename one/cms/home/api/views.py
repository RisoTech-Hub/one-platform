from one.cms.home.api.serializers import CMSHomeSerializer
from one.cms.home.models import CMSHome
from one.components.viewsets import BaseModelViewSet


class CMSHomeViewSet(BaseModelViewSet):
    queryset = CMSHome.objects.all()
    serializer_class = CMSHomeSerializer
