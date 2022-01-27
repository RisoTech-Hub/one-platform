from django.views.generic import DetailView, UpdateView

from one.components.constants import (
    EXCLUDE_FIELDS,
    FORM_LAYOUT_1_COL,
    FORM_LAYOUT_2_COL,
)


class ExposeDetailView(DetailView):
    """Auto add model fields to context"""

    def get(self, request, *args, **kwargs):
        """add model fields to context"""
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        fields = [
            field
            for field in self.model._meta.get_fields(include_parents=False)
            if field.concrete
            and not (
                field.is_relation
                or field.one_to_one
                or (field.many_to_one and field.related_model)
            )
            and field.name not in EXCLUDE_FIELDS
        ]
        context["fields"] = fields
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
