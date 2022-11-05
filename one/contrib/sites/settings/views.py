from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.models import Site
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from one.components.views import SuccessMessageMixin

from .forms import SettingForm, SiteForm


class SiteDetailView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "app/update.html"
    model = Site

    form_class = SiteForm
    success_message = _("Site successfully updated")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("Site Update")
        kwargs["page_breadcrumb"] = [
            {"name": _("Home"), "url": reverse("home")},
            {"name": _("Site Update"), "url": ""},
        ]

        kwargs["form_title"] = _("Site Update")

        if self.request.method == "POST":
            setting_form = SettingForm(
                self.request.POST, self.request.FILES, instance=self.object.setting
            )
        else:
            setting_form = SettingForm(instance=self.object.setting)
        kwargs["nested_forms"] = [
            {
                "form": setting_form,
                "title": _("Site Settings"),
            }
        ]
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("settings:site")

    def get_object(self):  # noqa
        return Site.objects.get_current()

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
            messages.error(request, _("Step Images has error"))
        return self.form_invalid(form)


site_detail_view = SiteDetailView.as_view()
