"""Declare Forms here."""
from django.conf import settings
from django.forms import ChoiceField, ModelForm, inlineformset_factory

from one.components.forms import CharField, FloatingLabelChoiceField
from one.components.widgets import SelectTwo
from one.core.menu.models import Menu, MenuItem


class MenuForm(ModelForm):
    language = ChoiceField(
        choices=settings.LANGUAGES,
        widget=SelectTwo(),
    )
    name = CharField()

    class Meta:
        model = Menu
        fields = "__all__"


class MenuItemForm(ModelForm):
    # menu
    type = FloatingLabelChoiceField(choices=MenuItem.TYPE_CHOICES)
    label = CharField()
    link = CharField()
    icon = CharField()
    # unique_code

    class Meta:
        model = MenuItem
        fields = "__all__"


MenuItemFormSet = inlineformset_factory(Menu, MenuItem, form=MenuItemForm, extra=10)
