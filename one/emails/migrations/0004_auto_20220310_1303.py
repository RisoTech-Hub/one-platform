# Generated by Django 3.2.12 on 2022-03-10 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emails", "0003_init_data"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="emailtemplate",
            options={
                "permissions": [("list_emailtemplate", "Can list email template")]
            },
        ),
        migrations.AlterField(
            model_name="emailtemplate",
            name="language",
            field=models.CharField(
                choices=[("vi", "Vietnamese"), ("en", "English")],
                default="vi",
                max_length=2,
                verbose_name="Language",
            ),
        ),
    ]
