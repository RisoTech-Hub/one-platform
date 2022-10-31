from django.contrib.auth.models import Group
from django_filters import CharFilter, FilterSet


class GroupFilter(FilterSet):
    name = CharFilter(lookup_expr="contains")

    class Meta:
        model = Group
        fields = ["name"]
