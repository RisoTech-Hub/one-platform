from django.conf import settings
from django.db import migrations


def add_email_template_forward(apps, schema_editor):
    """Auto create Email template"""
    EmailTemplate = apps.get_model("emails", "EmailTemplate")

    subjects = {
        "allauth_signup": "account/email/email_confirmation_signup",
        "allauth_reset": "account/email/password_reset_key",
        "allauth_confirm": "account/email/email_confirmation",
        "allauth_unknown": "account/email/unknown_account",
    }
    path = settings.TEMPLATES[0]["DIRS"][0]

    for subject in subjects:
        EmailTemplate.objects.create(
            code=subject,
            language="en",
            subject=open(
                "{0}/{1}_subject.txt".format(path, subjects[subject]),
                "r",
                encoding="utf-8",
            ).read(),
            content=open(
                "{0}/{1}_message.html".format(path, subjects[subject]),
                "r",
                encoding="utf-8",
            ).read(),
        )


def add_email_template_backward(apps, schema_editor):
    """Delete all Email template"""
    EmailTemplate = apps.get_model("emails", "EmailTemplate")
    EmailTemplate.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("emails", "0002_emailtemplate_subject")]

    operations = [
        migrations.RunPython(add_email_template_forward, add_email_template_backward)
    ]
