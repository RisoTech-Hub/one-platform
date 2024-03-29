from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView

from one.components.views import FormMixin, ListView, SuccessMessageMixin
from one.core.menu.menu import Menu as RegistedMenu

from .actions import get_core_menu_add
from .api.serializers import MenuSerializer
from .filters import MenuFilter
from .forms import MenuForm, MenuItemFormSet
from .models import Menu


class MenuCreateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, CreateView):
    template_name = "app/create.html"
    model = Menu

    form_class = MenuForm
    serializer_class = MenuSerializer

    success_message = _("Menu created successfully")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("Menu Create")
        kwargs["page_breadcrumb"] = [
            {"name": _("Menus"), "url": reverse("menu:menu-list")},
        ]

        kwargs["form_title"] = _("Menu Form")
        kwargs["hidden_fields"] = ["render"]
        if self.request.POST:
            menu_item_formset = MenuItemFormSet(self.request.POST, prefix="items")
        else:
            menu_item_formset = MenuItemFormSet(prefix="items")

        kwargs["formset"] = {
            "formset": menu_item_formset,
            "title": _("Menu Items"),
            "hidden_fields": ["unique_code"],
            "prefix": "items",
        }
        kwargs["formsets"] = [
            {
                "formset": menu_item_formset,
                "title": _("Menu Items"),
                "hidden_fields": ["unique_code"],
                "prefix": "items",
            }
        ]

        kwargs["registed_menu_items"] = RegistedMenu.process()

        kwargs["col"] = 2
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("menu:menu-list")

    def get_template_names(self):
        if self.request.GET.get("modern", None):
            return ["menu/menu-drag-drop.html"]
        return super().get_template_names()  # noqa


menu_create_view = MenuCreateView.as_view()


class MenuListView(LoginRequiredMixin, ListView):
    template_name = "app/list.html"
    model = Menu

    table_exclude_fields = ["render"]

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("Menu List")

        kwargs["actions"] = [get_core_menu_add()]

        kwargs["urls"] = {
            "update": "menu:menu-update",
        }

        kwargs["api_urls"] = {
            "list": "api:menu-list",
            "delete": "api:menu-delete",
        }
        kwargs["filter"] = MenuFilter()
        return kwargs


menu_list_view = MenuListView.as_view()


class MenuUpdateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, UpdateView):
    template_name = "app/update.html"
    model = Menu

    form_class = MenuForm
    serializer_class = MenuSerializer
    success_message = _("Menu successfully updated")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("Menu Update")
        kwargs["page_breadcrumb"] = [
            {"name": _("Menus"), "url": reverse("menu:menu-list")},
        ]

        kwargs["form_title"] = _("Menu Update")
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("menu:menu-list")

    def get_template_names(self):
        if self.request.GET.get("modern", None):
            return ["menu/menu-drag-drop.html"]
        return super().get_template_names()  # noqa


menu_update_view = MenuUpdateView.as_view()
