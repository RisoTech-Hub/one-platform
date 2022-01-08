from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Riso Tech one platform."""

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

    @property
    def display_name_html(self):
        return self.name if self.name else self.username

    @property
    def display_level_html(self):
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
