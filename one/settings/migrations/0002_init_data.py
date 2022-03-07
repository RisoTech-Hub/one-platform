from django.db import migrations


def setting_forward(apps, schema_editor):
    """Auto create Default setting"""
    Setting = apps.get_model("settings", "Setting")
    Setting.objects.create(
        name="Default", is_active=True, main_logo="/static/media/logos/logo-1-dark.svg"
    )


def setting_backward(apps, schema_editor):
    """Delete all Setting if create create fail"""
    Setting = apps.get_model("settings", "Setting")
    Setting.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("settings", "0001_initial")]

    operations = [migrations.RunPython(setting_forward, setting_backward)]
