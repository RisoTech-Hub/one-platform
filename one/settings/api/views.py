from one.components.viewsets import BaseModelViewSet
from one.settings.api.serializers import SettingSerializer
from one.settings.models import Setting


class SettingViewSet(BaseModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
