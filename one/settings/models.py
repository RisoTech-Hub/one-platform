from django.core.cache import cache
from django.db.models import BooleanField, CharField, ImageField
from django.utils.translation import gettext_lazy as _

from one.components.models import BaseModel
from one.settings.utils import logo_directory_path


class Setting(BaseModel):
    """
    Setting for Dashboard

    name: CharField, Specific code for core app
    main_logo: ImageField, path of main logo
    is_active: BooleanField, only one active at time
    """

    name = CharField(_("Name of setting"), max_length=1000, blank=True, null=True)
    is_active = BooleanField(_("Is active"), default=False)
    main_logo = ImageField(
        _("Dashboard main logo"), blank=True, null=True, upload_to=logo_directory_path
    )

    def activated(self):
        """
        Activate this instance then deactivate everything else
        :return:
        """
        Setting.objects.all().update(is_active=False)
        self.is_active = True
        self.save()
        cache.set("ACTIVE_SETTING", self, None)
