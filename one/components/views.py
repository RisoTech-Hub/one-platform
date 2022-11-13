import json

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db.models import ManyToManyField, ManyToManyRel, ManyToOneRel
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView as BaseCreateView
from django.views.generic import ListView as BaseListView
from django.views.generic.edit import FormMixin as BaseFormMixin

from .constants import FORM_TYPE_FULL, FORM_TYPE_QUICK


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
    is_popup = None
    quick_form_class = None
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
        if form_type.upper() == FORM_TYPE_QUICK and self.quick_form_class:
            return self.quick_form_class
        elif form_type.upper() == FORM_TYPE_FULL and self.form_class:
            return self.form_class
        else:
            return super().get_form_class()

    def get_template_names(self):
        if self.is_popup:
            return ["forms/quick-add-form.html"]
        return super().get_template_names()  # noqa

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
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["hidden_fields"] = ["creator", "last_modified_by"]
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user  # noqa
        return initial | {"creator": user} | {"last_modified_by": user}


class ListView(BaseListView):
    table_exclude_fields = []
    table_exclude_rel = [ManyToManyRel, ManyToOneRel, ManyToManyField]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table_fields"] = self.get_table_fields()
        context["content_type"] = ContentType.objects.get_for_model(self.model)
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
