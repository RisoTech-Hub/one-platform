# Generated by Django 4.0.8 on 2022-11-07 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contexts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="context",
            options={"verbose_name": "Context", "verbose_name_plural": "Contexts"},
        ),
    ]
