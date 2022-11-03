from allauth.account.views import AccountInactiveView as BaseAccountInactiveView
from allauth.account.views import ConfirmEmailView as BaseConfirmEmailView
from allauth.account.views import (
    EmailVerificationSentView as BaseEmailVerificationSentView,
)
from allauth.account.views import EmailView as BaseEmailView
from allauth.account.views import LoginView as BaseLoginView
from allauth.account.views import LogoutView as BaseLogoutView
from allauth.account.views import PasswordChangeView as BasePasswordChangeView
from allauth.account.views import PasswordResetDoneView as BasePasswordResetDoneView
from allauth.account.views import (
    PasswordResetFromKeyDoneView as BasePasswordResetFromKeyDoneView,
)
from allauth.account.views import (
    PasswordResetFromKeyView as BasePasswordResetFromKeyView,
)
from allauth.account.views import PasswordResetView as BasePasswordResetView
from allauth.account.views import PasswordSetView as BasePasswordSetView
from allauth.account.views import SignupView as BaseSignupView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin

from one.extend.metronic import KTLayout, KTTheme


class MetronicView(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)  # noqa
        context.update(
            {
                "layout": KTTheme.set_layout("auth.html", context),
            }
        )
        return context


class LoginView(MetronicView, BaseLoginView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        KTTheme.add_javascript_file("js/allauth/signin.js")  # noqa
        return context


login = LoginView.as_view()


class SignupView(MetronicView, BaseSignupView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        KTTheme.add_javascript_file("js/allauth/signup.js")  # noqa
        return context


signup = SignupView.as_view()


class ConfirmEmailView(BaseConfirmEmailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)  # noqa
        context.update(
            {
                "layout": KTTheme.set_layout("auth.html", context),  # noqa
            }
        )
        return context


confirm_email = ConfirmEmailView.as_view()


class EmailView(BaseEmailView):
    success_url = reverse_lazy("users:redirect")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)  # noqa
        context.update(
            {
                "layout": KTTheme.set_layout("default.html", context),  # noqa
            }
        )
        return context


email = login_required(EmailView.as_view())


class PasswordChangeView(MetronicView, BasePasswordChangeView):
    success_url = reverse_lazy("users:redirect")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        KTTheme.add_javascript_file("js/allauth/password-change.js")  # noqa
        return context


password_change = login_required(PasswordChangeView.as_view())


class PasswordSetView(MetronicView, BasePasswordSetView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        KTTheme.add_javascript_file("js/allauth/password-set.js")  # noqa
        return context


password_set = login_required(PasswordSetView.as_view())


class PasswordResetView(MetronicView, BasePasswordResetView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        KTTheme.add_javascript_file("js/allauth/password-reset.js")  # noqa
        return context


password_reset = PasswordResetView.as_view()


class PasswordResetDoneView(MetronicView, BasePasswordResetDoneView):
    pass


password_reset_done = PasswordResetDoneView.as_view()


class PasswordResetFromKeyView(MetronicView, BasePasswordResetFromKeyView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        KTTheme.add_javascript_file("js/allauth/password-reset-from-key.js")  # noqa
        return context


password_reset_from_key = PasswordResetFromKeyView.as_view()


class PasswordResetFromKeyDoneView(MetronicView, BasePasswordResetFromKeyDoneView):
    pass


password_reset_from_key_done = PasswordResetFromKeyDoneView.as_view()


class LogoutView(MetronicView, BaseLogoutView):
    pass


logout = LogoutView.as_view()


class AccountInactiveView(MetronicView, BaseAccountInactiveView):
    pass


account_inactive = AccountInactiveView.as_view()


class EmailVerificationSentView(MetronicView, BaseEmailVerificationSentView):
    pass


email_verification_sent = EmailVerificationSentView.as_view()
