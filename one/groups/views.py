from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView

from one.components.constants import FORM_LAYOUT_1_COL
from one.components.views import ExposeDetailView, WidgetUpdateView


class GroupListView(LoginRequiredMixin, ListView):
    model = Group


group_list_view = GroupListView.as_view()


class GroupDetailView(LoginRequiredMixin, ExposeDetailView):
    model = Group
    slug_field = "id"
    slug_url_kwarg = "id"


group_detail_view = GroupDetailView.as_view()


class GroupUpdateView(LoginRequiredMixin, SuccessMessageMixin, WidgetUpdateView):
    model = Group
    fields = "__all__"
    layout = FORM_LAYOUT_1_COL
    slug_field = "id"
    slug_url_kwarg = "id"
    read_only_fields = []


group_update_view = GroupUpdateView.as_view()
