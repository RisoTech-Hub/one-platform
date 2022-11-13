"""Declare Forms here."""
from django.forms import inlineformset_factory

from one.components.forms import CharField, ModelForm
from one.core.dynamic.models import Field, FieldSchema


class FieldSchemaForm(ModelForm):
    name = CharField()

    class Meta:
        model = FieldSchema
        fields = "__all__"


class FieldForm(ModelForm):
    class Meta:
        model = Field
        fields = "__all__"


FieldFormSet = inlineformset_factory(FieldSchema, Field, form=FieldForm, extra=1)
