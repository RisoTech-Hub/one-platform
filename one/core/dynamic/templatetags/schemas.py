from django.template import Library

register = Library()


@register.inclusion_tag("dynamic/choices.html")
def field_schema_choices(content_type):
    """
    Renders a list of choices for a given field schema.
    """
    if content_type:
        return {
            "schemas": content_type.field_schemas.all(),
        }
    return {"schemas": []}
