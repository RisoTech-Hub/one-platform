from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from one.users.utils import user_avatar_directory_path


class User(AbstractUser):
    """
    Default custom user model for Riso Tech one platform.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    dob = DateField(_("Day of birth"), blank=True, null=True)
    avatar = ImageField(
        _("Avatar of User"), blank=True, null=True, upload_to=user_avatar_directory_path
    )
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def display_name_html(self):
        """Get name or username"""
        return self.name if self.name else self.username

    @property
    def display_level_html(self):
        """Get level html"""
        if self.is_superuser:
            return """
                <span class='badge badge-light-danger fw-bolder fs-8 px-2 py-1
                '>Administrator</span>
            """
        elif self.is_staff:
            return """
                <span class='badge badge-light-warning fw-bolder fs-8 px-2 py-1
                '>Staff
                </span>
            """
        else:
            return """
                <span class='badge badge-light-info fw-bolder fs-8 px-2 py-1
                '>Member</span>
            """

    @property
    def is_notification_subcribe(self):
        """Webpush subscribe"""
        return self.webpush_info.all().count() > 0
