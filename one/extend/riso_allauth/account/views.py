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


class LoginView(BaseLoginView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


login = LoginView.as_view()


class SignupView(BaseSignupView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


signup = SignupView.as_view()


class ConfirmEmailView(BaseConfirmEmailView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


confirm_email = ConfirmEmailView.as_view()


class EmailView(BaseEmailView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


email = login_required(EmailView.as_view())


class PasswordChangeView(BasePasswordChangeView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


password_change = login_required(PasswordChangeView.as_view())


class PasswordSetView(BasePasswordSetView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


password_set = login_required(PasswordSetView.as_view())


class PasswordResetView(BasePasswordResetView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


password_reset = PasswordResetView.as_view()


class PasswordResetDoneView(BasePasswordResetDoneView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


password_reset_done = PasswordResetDoneView.as_view()


class PasswordResetFromKeyView(BasePasswordResetFromKeyView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


password_reset_from_key = PasswordResetFromKeyView.as_view()


class PasswordResetFromKeyDoneView(BasePasswordResetFromKeyDoneView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


password_reset_from_key_done = PasswordResetFromKeyDoneView.as_view()


class LogoutView(BaseLogoutView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


logout = LogoutView.as_view()


class AccountInactiveView(BaseAccountInactiveView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


account_inactive = AccountInactiveView.as_view()


class EmailVerificationSentView(BaseEmailVerificationSentView):
    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        return ret


email_verification_sent = EmailVerificationSentView.as_view()
