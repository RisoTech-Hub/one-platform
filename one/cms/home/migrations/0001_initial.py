# Generated by Django 4.0.8 on 2022-11-09 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CMSHome",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created on"
                    ),
                ),
                (
                    "time_modified",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Last modified on"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Title"
                    ),
                ),
                ("dynamic", models.JSONField(default=dict)),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Name"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created by",
                    ),
                ),
                (
                    "last_modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_last_modified_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Last modified by",
                    ),
                ),
            ],
            options={
                "verbose_name": "CMS Home",
                "verbose_name_plural": "CMS Home",
            },
        ),
    ]
