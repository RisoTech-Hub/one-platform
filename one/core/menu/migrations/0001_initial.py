# Generated by Django 4.0.8 on 2022-11-17 03:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name of Menu")),
                (
                    "render",
                    models.JSONField(
                        blank=True, default=dict, null=True, verbose_name="Render Json"
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("top", "Top"),
                            ("bottom", "Bottom"),
                            ("sidebar", "Sidebar"),
                        ],
                        default="sidebar",
                        max_length=255,
                        verbose_name="Position",
                    ),
                ),
            ],
            options={
                "verbose_name": "Menu",
                "verbose_name_plural": "Menus",
            },
        ),
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Item ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("link", "Link"),
                            ("accordion", "Accordion"),
                            ("section", "Section"),
                        ],
                        max_length=10,
                        verbose_name="Type of Item",
                    ),
                ),
                (
                    "label",
                    models.CharField(max_length=255, verbose_name="Label of Item"),
                ),
                (
                    "link",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Link of Item",
                    ),
                ),
                (
                    "icon",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Icon of Item",
                    ),
                ),
                (
                    "unique_code",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Unique Code of Item",
                    ),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="menu.menu",
                    ),
                ),
            ],
            options={
                "verbose_name": "Menu Item",
                "verbose_name_plural": "Menu Items",
            },
        ),
    ]
