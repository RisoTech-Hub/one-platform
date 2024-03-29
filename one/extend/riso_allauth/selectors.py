from django.template import Context, Template

from .models import AllauthTemplate


def context_render_from_template(code, context, subject_context):
    try:
        email_template = AllauthTemplate.objects.filter(code=code).last()
        content_template = Template(email_template.content)
        subject_template = Template(email_template.subject)
        return (
            subject_template.render(Context(subject_context)),
            content_template.render(Context(context)),
        )
    except AllauthTemplate.DoesNotExist:
        return None, None
