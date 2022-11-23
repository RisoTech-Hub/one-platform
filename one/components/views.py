import json

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db.models import ManyToManyField, ManyToManyRel, ManyToOneRel
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView as BaseCreateView
from django.views.generic import ListView as BaseListView
from django.views.generic import UpdateView as BaseUpdateView
from django.views.generic.edit import FormMixin as BaseFormMixin

from one.components.constants import (
    FORM_TYPE_PAGE,
    FORM_TYPE_POPUP,
    TAB_GROUP_DYNAMIC,
    TAB_GROUP_GENERAL,
    TAB_GROUP_HIDDEN,
    TAB_GROUP_SEO,
)


class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """

    is_popup = False
    success_message = ""

    def form_valid(self, form, *args, **kwargs):
        response = super().form_valid(form)  # noqa
        success_message = self.get_success_message(form.cleaned_data)
        is_nested = kwargs.get("is_nested", False)
        if success_message and not self.is_popup and not is_nested:  # noqa
            messages.success(self.request, success_message)  # noqa
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class FormMixin(BaseFormMixin):
    popup_template_name = "forms/popup_form.html"
    is_popup = None
    popup_form_class = None
    form_class = None
    serializer_class = None

    def setup(self, request, *args, **kwargs):
        self.is_popup = request.GET.get("popup", None)
        super().setup(request, *args, **kwargs)  # noqa

    def add_error_messages(self, form):
        errors = json.loads(form.errors.as_json())
        if errors:
            for error in errors:
                messages.error(self.request, errors[error][0]["message"])  # noqa

    def get_form_class(self):
        form_type = self.request.GET.get("form_type", None)  # noqa
        if not form_type:
            return super().get_form_class()
        if form_type.upper() == FORM_TYPE_POPUP and self.popup_form_class:
            return self.popup_form_class
        elif form_type.upper() == FORM_TYPE_PAGE and self.form_class:
            return self.form_class
        else:
            return super().get_form_class()

    def get_template_names(self):
        return (
            [self.popup_template_name]
            if self.is_popup
            else super().get_template_names()  # noqa
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ("POST", "PUT"):  # noqa
            kwargs["request"] = self.request  # noqa
        return kwargs

    def form_invalid(self, form):
        if self.is_popup:
            return JsonResponse({"errors": form.errors}, status=400)
        return super().form_invalid(form)

    def form_valid(self, form):
        super().form_valid(form)
        if self.is_popup:  # noqa
            try:
                return JsonResponse(
                    self.serializer_class(
                        self.object,  # noqa
                    ).data,
                    status=201,
                )
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
        return HttpResponseRedirect(self.get_success_url())


class CreateView(BaseCreateView):
    template_name = "app/create.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["hidden_fields"] = ["creator", "last_modified_by", "schema_id"]
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user  # noqa
        return initial | {"creator": user} | {"last_modified_by": user}


class TabCreateView(CreateView):
    template_name = "app/create_tabs.html"

    tabs = []
    hidden_tabs = []

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        active_tab = self.request.GET.get("active_tab", None)
        kwargs["active_tab"] = active_tab if active_tab else TAB_GROUP_GENERAL
        kwargs["hidden_tabs"] = (
            self.hidden_tabs if self.hidden_tabs else [TAB_GROUP_HIDDEN]
        )
        kwargs["tabs"] = (
            self.tabs + [TAB_GROUP_HIDDEN]
            if self.tabs
            else [TAB_GROUP_HIDDEN, TAB_GROUP_GENERAL, TAB_GROUP_DYNAMIC, TAB_GROUP_SEO]
        )
        return kwargs


class ListView(BaseListView):
    template_name = "app/list.html"

    # Filter
    filter_class = None

    # Datatable
    table_exclude_fields = []
    table_exclude_rel = [ManyToManyRel, ManyToOneRel, ManyToManyField]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table_fields"] = self.get_table_fields()
        context["content_type"] = ContentType.objects.get_for_model(self.model)
        context["filter"] = self.filter_class() if self.filter_class else None
        return context

    def get_table_fields(self):
        fields = self.model._meta.get_fields()  # noqa
        data = []
        for field in fields:
            if not field.is_relation and not (
                field.name in self.table_exclude_fields + ["password"]
            ):
                data.append(
                    {
                        "col_name": field.name,
                        "verbose_name": field.verbose_name,
                        "order": 0 if field.name == "id" else 1,
                    }
                )
            elif (
                field.is_relation
                and not (type(field) in self.table_exclude_rel)
                and not (field.related_model is self.model)
                and not (field.name in self.table_exclude_fields + ["password"])
            ):
                nested_fields = field.related_model._meta.get_fields()  # noqa
                for nested_field in nested_fields:
                    if not nested_field.is_relation and not (
                        nested_field.name
                        in self.table_exclude_fields + ["password", "id"]
                    ):
                        data.append(
                            {
                                "col_name": f"{field.name}.{nested_field.name}",
                                "verbose_name": nested_field.verbose_name,
                                "order": 1,
                            }
                        )
            else:
                pass
        return sorted(data, key=lambda item: item["order"])


class UpdateView(BaseUpdateView):
    template_name = "app/update.html"

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["hidden_fields"] = ["creator", "last_modified_by", "schema_id"]
        return kwargs


class TabUpdateView(UpdateView):
    template_name = "app/update_tabs.html"

    tabs = []
    hidden_tabs = []

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        active_tab = self.request.GET.get("active_tab", None)
        kwargs["active_tab"] = active_tab if active_tab else TAB_GROUP_GENERAL
        kwargs["hidden_tabs"] = (
            self.hidden_tabs if self.hidden_tabs else [TAB_GROUP_HIDDEN]
        )
        kwargs["tabs"] = (
            self.tabs
            if self.tabs
            else [TAB_GROUP_HIDDEN, TAB_GROUP_GENERAL, TAB_GROUP_DYNAMIC, TAB_GROUP_SEO]
        )
        return kwargs
