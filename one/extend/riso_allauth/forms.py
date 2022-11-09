from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from tinymce.widgets import TinyMCE

from one.components.forms import CharField, ModelForm
from one.extend.riso_allauth.models import AllauthTemplate


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class TemplateForm(ModelForm):
    subject = CharField()
    content = CharField(widget=TinyMCE())

    class Meta:
        model = AllauthTemplate
        fields = ["subject", "content"]
