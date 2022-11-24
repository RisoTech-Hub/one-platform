from django.contrib.sites.models import Site
from django.db.models import CASCADE, ImageField, Model, OneToOneField
from django.utils.translation import gettext_lazy as _

from one.contrib.sites.settings.utils import setting_images_directory_path


class Setting(Model):
    """Setting model is OneToOne related to Site model."""

    site = OneToOneField(
        Site,
        on_delete=CASCADE,
        primary_key=True,
        related_name="setting",
        verbose_name="site",
    )

    favicon = ImageField(
        _("Favicon of site"),
        blank=True,
        null=True,
        upload_to=setting_images_directory_path,
    )
    logo = ImageField(
        _("Logo of site"),
        blank=True,
        null=True,
        upload_to=setting_images_directory_path,
    )
    dark_logo = ImageField(
        _("Dark Logo of site"),
        blank=True,
        null=True,
        upload_to=setting_images_directory_path,
    )
    small_logo = ImageField(
        _("Small Logo of site"),
        blank=True,
        null=True,
        upload_to=setting_images_directory_path,
    )
    mobile_logo = ImageField(
        _("Mobile logo of site"),
        blank=True,
        null=True,
        upload_to=setting_images_directory_path,
    )

    class Meta:
        app_label = "sites"
        verbose_name = _("Site Setting")
        verbose_name_plural = _("Site Settings")
        db_table = "django_site_setting"

    def __str__(self):
        return self.site.name

    @property
    def favicon_url(self):
        """Return logo url"""
        return (
            "/static/metronic/media/logos/logo-1-dark.svg"
            if not self.favicon
            else getattr(self.favicon, "url")
        )

    @property
    def logo_url(self):
        """Return logo url"""
        return (
            "/static/metronic/media/logos/logo-1-dark.svg"
            if not self.logo
            else getattr(self.logo, "url")
        )

    @property
    def dark_logo_url(self):
        """Return logo url"""
        return (
            "/static/metronic/media/logos/logo-1-dark.svg"
            if not self.dark_logo
            else getattr(self.dark_logo, "url")
        )

    @property
    def small_logo_url(self):
        """Return logo url"""
        return (
            "/static/metronic/media/logos/logo-1-dark.svg"
            if not self.small_logo
            else getattr(self.small_logo, "url")
        )

    @property
    def mobile_logo_url(self):
        """Return mobile_logo url"""
        return (
            "/static/metronic/media/logos/logo-2.svg"
            if not self.mobile_logo
            else getattr(self.mobile_logo, "url")
        )
