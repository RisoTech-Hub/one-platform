"""Declare Forms here."""
from django.conf import settings
from django.forms import ChoiceField, inlineformset_factory

from one.components.forms import CharField, FloatingLabelChoiceField, ModelForm
from one.components.widgets import SelectTwo
from one.core.menu.models import Menu, MenuItem


class MenuForm(ModelForm):
    language = ChoiceField(
        choices=settings.LANGUAGES,
        widget=SelectTwo(),
    )
    name = CharField()
    position = ChoiceField(
        choices=Menu.POSITION_CHOICES,
        widget=SelectTwo(),
    )

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


MenuItemFormSet = inlineformset_factory(Menu, MenuItem, form=MenuItemForm, extra=1)
