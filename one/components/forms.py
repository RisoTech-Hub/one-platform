from django.forms import CharField as BaseCharField
from django.forms import ChoiceField as BaseChoiceField
from django.forms import ImageField as BaseImageField
from django.forms import JSONField
from django.forms import ModelForm as BaseModelForm

from one.components.widgets import (
    BootstrapInput,
    FloatingLabelSelectTwo,
    ImageInput,
    JSONEditorWidget,
)


class CharField(BaseCharField):
    widget = BootstrapInput


class ImageField(BaseImageField):
    widget = ImageInput


class FloatingLabelChoiceField(BaseChoiceField):
    widget = FloatingLabelSelectTwo


class ModelForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)


class DynamicForm(ModelForm):
    dynamic = JSONField(required=False, widget=JSONEditorWidget())

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
