from django.contrib.auth.mixins import LoginRequiredMixin

from one.components.views import ExposeListView
from one.settings.models import Setting


class SettingListView(LoginRequiredMixin, ExposeListView):
    model = Setting


setting_list_view = SettingListView.as_view()
