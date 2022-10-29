import json

from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic.edit import FormMixin as BaseFormMixin

from .constants import FORM_TYPE_FULL, FORM_TYPE_QUICK


class FormMixin(BaseFormMixin):
    is_popup = None
    quick_form_class = None
    form_class = None
    serializer_class = None

    def setup(self, request, *args, **kwargs):
        self.is_popup = request.GET.get("popup", None)
        super().setup(request, *args, **kwargs)

    def get_form_class(self):
        form_type = self.request.GET.get("form_type", None)
        if not form_type:
            return super().get_form_class()
        if form_type.upper() == FORM_TYPE_QUICK and self.quick_form_class:
            return self.quick_form_class
        elif form_type.upper() == FORM_TYPE_FULL and self.form_class:
            return self.form_class
        else:
            return super().get_form_class()

    def add_error_messages(self, form):
        errors = json.loads(form.errors.as_json())
        if errors:
            for error in errors:
                messages.error(self.request, errors[error][0]["message"])

    def form_invalid(self, form):
        if self.is_popup:
            return JsonResponse({"errors": form.errors}, status=400)
        self.add_error_messages(form)
        return super().form_invalid(form)

    def form_valid(self, form):
        super().form_valid(form)
        if self.is_popup:  # noqa
            try:
                return JsonResponse(
                    self.serializer_class(self.object).data, status=201  # noqa
                )
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
        return HttpResponseRedirect(self.get_success_url())
