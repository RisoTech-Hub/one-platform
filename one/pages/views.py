from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from one.components.constants import FORM_LAYOUT_2_COL
from one.components.views import WidgetUpdateView
from one.pages.models import Page


class PageUpdateView(LoginRequiredMixin, SuccessMessageMixin, WidgetUpdateView):
    model = Page
    fields = "__all__"
    layout = FORM_LAYOUT_2_COL
    read_only_fields = ["url"]


page_update_view = PageUpdateView.as_view()
