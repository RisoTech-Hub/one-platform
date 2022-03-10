from django.conf import settings
from django.db import migrations


def add_page_forward(apps, schema_editor):
    """Auto create Page"""
    Page = apps.get_model("pages", "Page")

    template = str(settings.APPS_DIR / "templates")

    Page.objects.create(
        name="Homepage",
        url="/",
        language="en",
        is_active=True,
        content=open(
            f"{template}/pages/home.html",
            "r",
            encoding="utf-8",
        ).read(),
    )

    Page.objects.create(
        name="About",
        url="/about/",
        language="en",
        is_active=True,
        content=open(
            f"{template}/pages/about.html",
            "r",
            encoding="utf-8",
        ).read(),
    )


def add_page_backward(apps, schema_editor):
    """Delete all Page"""
    Page = apps.get_model("pages", "Page")
    Page.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("pages", "0001_initial")]

    operations = [migrations.RunPython(add_page_forward, add_page_backward)]
