from one.cms.home.models import CMSHome
from one.components.forms import DynamicForm


class CMSHomeForm(DynamicForm):
    class Meta:
        model = CMSHome
        fields = "__all__"
