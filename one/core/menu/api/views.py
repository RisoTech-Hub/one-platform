from one.components.viewsets import BaseModelViewSet
from one.core.menu.api.serializers import MenuSerializer
from one.core.menu.models import Menu


class MenuViewSet(BaseModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
