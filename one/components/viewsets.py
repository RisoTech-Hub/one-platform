from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend


class FilterModelViewSet(ModelViewSet):
    """
    Add default url filter for ModelViewSet
    """

    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"
