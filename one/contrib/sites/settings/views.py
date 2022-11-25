from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from one.components.views import FormMixin, SuccessMessageMixin
from one.contrib.sites.settings.api.serializers import SiteSerializer
from one.contrib.sites.settings.forms import SettingForm, SiteForm


class SiteUpdateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, UpdateView):
    model = Site

    template_name = "app/update.html"
    popup_template_name = "forms/drawer_form.html"

    form_class = SiteForm
    serializer_class = SiteSerializer

    success_message = _("Site successfully updated")
    success_url = "/"

    is_popup = True

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["form_title"] = _("Update site settings")

        setting_form = SettingForm(instance=self.object.setting)
        if self.request.method == "POST":
            setting_form = SettingForm(
                self.request.POST, self.request.FILES, instance=self.object.setting
            )
        kwargs["nested_forms"] = [
            {
                "form": setting_form,
                "title": _("Site Settings"),
            }
        ]
        return kwargs

    def get_object(self):  # noqa
        return Site.objects.get_current(self.request)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = self.get_object()  # noqa
        setting_form = SettingForm(
            self.request.POST, self.request.FILES, instance=self.object.setting
        )
        form = self.get_form()
        if form.is_valid():
            if setting_form.is_valid():
                self.form_valid(setting_form, is_nested=True)
                return self.form_valid(form)
        return self.form_invalid(form)


site_update_view = SiteUpdateView.as_view()
