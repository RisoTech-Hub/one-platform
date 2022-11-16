from django.forms import CharField
from django.utils.translation import gettext_lazy as _

from one.cms.home.models import CMSHome
from one.components.forms import BaseForm, DynamicForm, SEOForm


class CMSHomeForm(DynamicForm, SEOForm, BaseForm):
    name = CharField()
    name.group = _("General")

    class Meta:
        model = CMSHome
        fields = "__all__"
