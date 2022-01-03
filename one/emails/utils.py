from django.template import Context, Template

from one.emails.models import EmailTemplate


def context_render_from_template(code, context, subject_context, language):
    """
    :param code:
    :param context:
    :param subject_context:
    :param language:
    :return: body of email based on code and context
    """
    try:
        email_template = EmailTemplate.objects.filter(
            code=code, language=language
        ).last()
        content_template = Template(email_template.content)
        subject_template = Template(email_template.subject)
        return (
            subject_template.render(Context(subject_context)),
            content_template.render(Context(context)),
        )
    except EmailTemplate.DoesNotExist:
        return None, None
