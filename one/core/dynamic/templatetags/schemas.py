from django.template import Library

register = Library()


# @register.inclusion_tag("attachments/add_form.html", takes_context=True)
# def attachment_form(context, obj, **kwargs):
#     """
#     Renders a "upload attachment" form.
#     The user must own ``attachments.add_attachment permission`` to add
#     attachments.
#     """
#     if context["user"].has_perm("attachments.add_attachment"):
#         return {
#             "form": AttachmentForm(),
#             "form_url": add_url_for_obj(obj),
#             "next": kwargs.get("next", context.request.build_absolute_uri()),
#         }
#     else:
#         return {"form": None}


@register.inclusion_tag("dynamic/choices.html")
def field_schema_choices(content_type):
    """
    Renders a list of choices for a given field schema.
    """
    return {
        "schemas": content_type.field_schemas.all(),
    }
