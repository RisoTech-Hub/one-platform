from django.http import Http404
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, UpdateView

from one.components.constants import FORM_LAYOUT_1_COL, FORM_LAYOUT_2_COL
from one.components.utils import _get_fields, _get_o2o_fields


class ExposeListView(ListView):
    """Auto add model fields to context of ListView"""

    def get(self, request, *args, **kwargs):
        """add model fields to context"""
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        context["fields"] = _get_fields(
            self.model._meta.get_fields(include_parents=False), ["id"]
        )
        context["nested_fields"] = _get_o2o_fields(
            self.model._meta.get_fields(include_parents=False)
        )
        return self.render_to_response(context)


class ExposeDetailView(DetailView):
    """Auto add model fields to context of DetailView"""

    def get(self, request, *args, **kwargs):
        """add model fields to context"""
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["fields"] = _get_fields(
            self.model._meta.get_fields(include_parents=False)
        )
        return self.render_to_response(context)


class WidgetUpdateView(UpdateView):
    """Override context data"""

    layout = FORM_LAYOUT_1_COL

    def get_context_data(self, **kwargs):
        """Auto add class to form field, and read only field"""
        kwargs = super(WidgetUpdateView, self).get_context_data(**kwargs)
        kwargs.update({"layout": self.layout})
        form = kwargs["form"]
        for field in form.fields:
            _field = form.fields[field]
            widget = _field.widget
            attrs = widget.attrs
            if widget.input_type == "text":
                _class = "form-control form-control-lg form-control-solid "
                if self.layout == FORM_LAYOUT_2_COL:
                    _class = "form-control form-control-solid active "
                if "class" in attrs:
                    attrs["class"] = _class + attrs["class"]
                else:
                    attrs.update({"class": _class})

            if widget.input_type == "textarea":
                attrs.update({"custom": "ble"})

        for field in self.read_only_fields:
            _field = form.fields[field]
            attrs = _field.widget.attrs
            attrs.update({"readonly": "readonly"})
        return kwargs
