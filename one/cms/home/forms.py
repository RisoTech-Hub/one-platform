from one.cms.home.models import CMSHome
from one.components.constants import TAB_GROUP_GENERAL
from one.components.fields import CharField
from one.components.forms import BaseForm, DynamicForm, SEOForm


class CMSHomeForm(DynamicForm, SEOForm, BaseForm):
    name = CharField()
    name.group = TAB_GROUP_GENERAL

    class Meta:
        model = CMSHome
        fields = "__all__"
