from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from one.components.filters import AllSearchFilter


class FilterModelViewSet(ModelViewSet):
    """
    Add default url filter for ModelViewSet
    """

    filter_backends = [DjangoFilterBackend, AllSearchFilter, OrderingFilter]
    filter_fields = "__all__"
    ordering_fields = "__all__"
