"""Declare Forms here."""
from django.forms import ChoiceField, inlineformset_factory

from one.components.fields import CharField
from one.components.forms import ModelForm
from one.components.widgets import BootstrapInput, FloatingLabelSelectTwo
from one.core.dynamic.constants import FIELD_TYPE_CHOICE_INPUT
from one.core.dynamic.models import Field, FieldSchema


class FieldSchemaForm(ModelForm):
    name = CharField()

    class Meta:
        model = FieldSchema
        fields = "__all__"


class FieldForm(ModelForm):
    name = CharField(widget=BootstrapInput(attrs={"placeholder": "Name"}))
    type = ChoiceField(choices=FIELD_TYPE_CHOICE_INPUT, widget=FloatingLabelSelectTwo())

    class Meta:
        model = Field
        fields = "__all__"


FieldFormSet = inlineformset_factory(FieldSchema, Field, form=FieldForm, extra=1)
