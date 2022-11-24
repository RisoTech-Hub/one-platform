# Generated by Django 4.0.8 on 2022-11-24 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Config",
            fields=[
                (
                    "contenttype",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="configs",
                        serialize=False,
                        to="contenttypes.contenttype",
                        verbose_name="Content Type",
                    ),
                ),
            ],
            options={
                "verbose_name": "Content Type",
                "verbose_name_plural": "Content Types",
                "db_table": "django_content_type_config",
            },
        ),
    ]
