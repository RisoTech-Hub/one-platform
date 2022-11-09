from random import randint
from uuid import uuid4

from django.conf import settings
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    JSONField,
    Manager,
    Model,
    UUIDField,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer

from .managers import LingualManager


class MetaModel(Model):
    class Meta:
        abstract = True

    class Metadata:
        avatar_field = None
        name_field = None
        title_field = None
        protect_flag_field = None

    @property
    def as_avatar(self):
        """Return object as Image url instead of __str__"""
        avatar = getattr(self, str(self.Metadata.avatar_field), None)
        return (
            f"/static/metronic/media/svg/shapes/abstract-{randint(1, 5)}-dark.svg"
            if not avatar
            else getattr(avatar, "url")
        )

    @property
    def as_name(self):
        """Return object as value of name field instead of __str__"""
        name = getattr(self, str(self.Metadata.name_field), None)
        return name if name else str(self)

    @property
    def as_title(self):
        """Return object as value of title field instead of __str__"""
        name = getattr(self, str(self.Metadata.title_field), None)
        return name if name else ""

    @property
    def as_choice(self):
        """Render object as image and name in choice"""
        image = "<img class='rounded-circle me-2' src='{self.as_avatar}' style='width: 26px;'>"
        return f"<span>{image}{self.as_name}</span>"

    @property
    def as_cell(self):
        """
        Render object as image and name and title in table cell
        """
        return (
            '<div class="d-flex align-items-center">'
            + '<div class="symbol symbol-45px me-5">'
            + f'<img alt="{self.as_name}" src="{self.as_avatar}">'
            + "</div>"
            + '<div class="d-flex justify-content-start flex-column">'
            + '<a href="#" class="text-dark fw-bolder text-hover-primary '
            + f'mb-1 fs-6">{self.as_name}</a>'
            + f'<span class="text-muted fw-bold text-muted d-block fs-7">{self.as_title}</span>'
            + "</div>"
            + "</div>"
        )

    @property
    def as_dict(self):
        """as_dict"""

        class ObjectSerializer(ModelSerializer):
            class Meta:
                model = type(self)
                fields = "__all__"
                depth = 1

        serializer = ObjectSerializer(self)
        return [
            {"key": item, "value": serializer.data.get(item)}
            for item in serializer.data
        ]


class BaseModel(MetaModel):
    id = UUIDField(_("ID"), primary_key=True, default=uuid4, editable=False)
    time_created = DateTimeField(
        verbose_name=_("Created on"), auto_now_add=True, null=True
    )
    time_modified = DateTimeField(
        verbose_name=_("Last modified on"), auto_now=True, null=True
    )
    creator = ForeignKey(
        "users.User",
        verbose_name=_("Created by"),
        related_name="%(app_label)s_%(class)s_creator",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )
    last_modified_by = ForeignKey(
        "users.User",
        verbose_name="Last modified by",
        related_name="%(app_label)s_%(class)s_last_modified_by",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.time_created:
            self.time_created = timezone.now()

        self.time_modified = timezone.now()
        return super().save(*args, **kwargs)


class LingualModel(Model):
    language = CharField(
        max_length=2,
        verbose_name=_("Language"),
        choices=settings.LANGUAGES,
        default=settings.VIETNAMESE,
    )
    lingual_objects = LingualManager()
    objects = Manager()

    class Meta:
        abstract = True

    @property
    def language_verbose(self):
        return dict(settings.LANGUAGES)[self.language]


class SEOModel(Model):
    title = CharField(max_length=255, verbose_name=_("Title"), null=True, blank=True)

    # description = CharField(
    #     max_length=255, verbose_name=_("Description"), null=True, blank=True
    # )
    # keywords = CharField(
    #     max_length=255, verbose_name=_("Keywords"), null=True, blank=True
    # )
    # og_title = CharField(
    #     max_length=255, verbose_name=_("OG Title"), null=True, blank=True
    # )
    # og_description = CharField(
    #     max_length=255, verbose_name=_("OG Description"), null=True, blank=True
    # )
    # og_image = ImageField(
    #     upload_to="og_images", verbose_name=_("OG Image"), null=True, blank=True
    # )
    # og_url = CharField(
    #     max_length=255, verbose_name=_("OG URL"), null=True, blank=True
    # )
    # og_type = CharField(
    #     max_length=255, verbose_name=_("OG Type"), null=True, blank=True
    # )
    # og_locale = CharField(
    #     max_length=255, verbose_name=_("OG Locale"), null=True, blank=True
    # )
    # og_site_name = CharField(
    #     max_length=255, verbose_name=_("OG Site Name"), null=True, blank=True
    # )
    # twitter_title = CharField(
    #     max_length=255, verbose_name=_("Twitter Title"), null=True, blank=True
    # )
    # twitter_description = CharField(
    #     max_length=255, verbose_name=_("Twitter Description"), null=True, blank=True
    # )
    # twitter_image = ImageField(
    #     upload_to="twitter_images",
    #     verbose_name=_("Twitter Image"),
    #     null=True,
    #     blank=True,
    # )
    # twitter_card = CharField(
    #     max_length=255, verbose_name=_("Twitter Card"), null=True, blank=True
    # )
    # twitter_site = CharField(
    #     max_length=255, verbose_name=_("Twitter Site"), null=True, blank=True
    # )
    # twitter_creator = CharField(
    #     max_length=255, verbose_name=_("Twitter Creator"), null=True, blank=True
    # )

    class Meta:
        abstract = True


class DynamicModel(Model):
    dynamic = JSONField(default=dict)

    class Meta:
        abstract = True
