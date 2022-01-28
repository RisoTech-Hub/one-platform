import datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for Riso Tech one platform.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def group_verbose(self):
        GROUP = {
            "Administrator": "danger",
            "Manager": "warning",
            "Leader": "success",
            "Sale": "info",
        }
        try:
            group = self.groups.first().name
            return GROUP[group]
        except KeyError:
            return "Non Group"

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
        if self.online:
            return "Online"
        return "Offline"
