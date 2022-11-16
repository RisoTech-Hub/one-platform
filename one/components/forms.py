from django.forms import JSONField, ModelChoiceField
from django.forms import ModelForm as BaseModelForm
from django.utils.translation import gettext_lazy as _

from one.components.fields import CharField
from one.components.widgets import BootstrapInput, JSONEditorWidget
from one.users.models import User


class ModelForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)


class BaseForm(ModelForm):
    creator = ModelChoiceField(queryset=User.objects.all(), required=False)
    creator.group = _("Hidden")
    last_modified_by = ModelChoiceField(queryset=User.objects.all(), required=False)
    last_modified_by.group = _("Hidden")


class SEOForm(ModelForm):
    title = CharField(required=True, widget=BootstrapInput())
    title.group = _("SEO")


class DynamicForm(ModelForm):
    schema_id = CharField(required=False, widget=BootstrapInput())
    schema_id.group = _("Dynamic")
    dynamic = JSONField(required=False, widget=JSONEditorWidget())
    dynamic.group = _("Dynamic")

    # def clean_extra_fields(self, *args, **kwargs):
    #     extra_fields = self.cleaned_data.get("extra_fields")
    #     if not self.extra_fields_list:
    #         return extra_fields
    #     for field in self.extra_fields_list:
    #         if field.field_mandatory:
    #             if any(
    #                 [
    #                     (field.field.field_code not in extra_fields),
    #                     (
    #                         field.field.field_code in extra_fields
    #                         and extra_fields.get(field.field.field_code, "") == ""
    #                     ),
    #                 ]
    #             ):
    #                 raise ValidationError(
    #                     _(f'Field "{field.field.field_name}" is required')
    #                 )
    #     return extra_fields
