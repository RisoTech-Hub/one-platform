from django.contrib.auth.models import Group

from one.components.fields import CharField, ImageField
from one.components.forms import ModelForm

from .models import Context


class ContextForm(ModelForm):
    avatar = ImageField(required=False)

    class Meta:
        model = Context
        exclude = ["group"]


class GroupForm(ModelForm):
    name = CharField()

    class Meta:
        model = Group
        fields = ["name"]
