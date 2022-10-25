import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView


class PopUpCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    is_popup = None

    def setup(self, request, *args, **kwargs):
        self.is_popup = request.GET.get("popup", None)
        super().setup(request, *args, **kwargs)

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
                    self.serializer_class(self.object).data, status=201
                )  # noqa
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)
        return HttpResponseRedirect(self.get_success_url())
