import datetime
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from django.db.models import CharField, DateField, ImageField, TextField, UUIDField
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

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    dob = DateField(_("Day of birth"), blank=True, null=True)
    avatar = ImageField(
        _("Avatar of User"), blank=True, null=True, upload_to=user_avatar_directory_path
    )

    status = TextField(_("Status of User"), blank=True, null=True)

    first_name = None  # type: ignore
    last_name = None  # type: ignore

    class Meta:
        permissions = [
            ("list_user", "Can list user"),
        ]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    # Properties
    @property
    def avatar_url(self):
        return (
            "/static/media/svg/avatars/blank.svg"
            if not self.avatar
            else self.avatar.url
        )

    # End Properties

    # Choice display
    @property
    def display_choice_html(self):
        image = f"<img class='rounded-circle me-2' src='{self.avatar_url}' style='width: 26px;'>"
        return f"<span>{image} {self.display_name_html}</span>"

    # End Choice display

    # User Active status
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

    def online_dot_verbose(self):
        if self.online():
            return """<div class="position-absolute translate-middle bottom-0 start-100 mb-6 bg-success rounded-circle
                      border border-4 border-white h-20px w-20px"></div>"""
        return """<div class="position-absolute translate-middle bottom-0 start-100 mb-6 bg-danger rounded-circle
                  border border-4 border-white h-20px w-20px"></div>"""

    # End User Active status

    # Browser Notification
    @property
    def is_notification_subcribe(self):
        """Webpush subscribe"""
        return self.webpush_info.all().count() > 0

    # End Browser Notification

    # Display as HTML
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
                '>{name}</span>"""
        elif self.is_staff:
            name = _("Staff")
            return f"""
                <span class='badge badge-light-warning fw-bolder fs-8 px-2 py-1
                '>{name}</span>"""
        else:
            name = _("Member")
            return f"""
                <span class='badge badge-light-info fw-bolder fs-8 px-2 py-1
                '>{name}</span>"""

    # End Display as HTML
