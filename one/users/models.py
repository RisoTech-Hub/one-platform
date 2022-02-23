import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from django.db.models import CharField, DateField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from one.users.utils import user_avatar_directory_path


class User(AbstractUser):
    """
    Default custom user model for Riso Tech one platform.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.

    name: CharField, Name of user
    dob: DateField, Date of birth
    avatar: ImageField, path of avatar
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    dob = DateField(_("Day of birth"), blank=True, null=True)
    avatar = ImageField(
        _("Avatar of User"), blank=True, null=True, upload_to=user_avatar_directory_path
    )
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    class Meta:
        permissions = [
            ("list_user", "Can get list of user"),
        ]

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
            name = _("Super User")
            return f"""
                <span class='badge badge-light-danger fw-bolder fs-8 px-2 py-1
                '>{name}</span>
            """
        elif self.is_staff:
            name = _("Staff")
            return f"""
                <span class='badge badge-light-warning fw-bolder fs-8 px-2 py-1
                '>{name}</span>
            """
        else:
            name = _("Member")
            return f"""
                <span class='badge badge-light-info fw-bolder fs-8 px-2 py-1
                '>{name}</span>
            """

    @property
    def is_notification_subcribe(self):
        """Webpush subscribe"""
        return self.webpush_info.all().count() > 0

    def active_verbose(self):
        if self.is_active:
            return "Active"
        return "Not Active"

    def last_seen(self):
        return cache.get("seen_%s" % self.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                seconds=settings.USER_ONLINE_TIMEOUT
            ):
                return False
            else:
                return True
        else:
            return False

    def online_verbose(self):
        if self.online():
            return "Online"
        return "Offline"
