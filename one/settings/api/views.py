from rest_framework.viewsets import ModelViewSet

from one.settings.api.serializers import SettingSerializer
from one.settings.models import Setting


class SettingViewSet(ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
