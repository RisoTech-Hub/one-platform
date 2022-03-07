from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView

from one.components.constants import FORM_LAYOUT_2_COL
from one.components.views import ExposeDetailView, WidgetUpdateView

User = get_user_model()


class ProfileDetailView(LoginRequiredMixin, ExposeDetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


profile_detail_view = ProfileDetailView.as_view()


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, WidgetUpdateView):

    model = User
    fields = ["name", "dob", "username", "avatar", "status"]
    success_message = _("Information successfully updated")
    layout = FORM_LAYOUT_2_COL
    read_only_fields = ["username"]

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


profile_update_view = ProfileUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
