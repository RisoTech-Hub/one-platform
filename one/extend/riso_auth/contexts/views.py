from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView

from one.components.views import FormMixin

from .api.serializers import GroupSerializer
from .forms import ContextForm, GroupForm


class GroupListView(LoginRequiredMixin, ListView):
    template_name = "app/list.html"
    model = Group


group_list_view = GroupListView.as_view()


class GroupCreateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, CreateView):
    template_name = "app/create.html"
    model = Group

    form_class = GroupForm
    serializer_class = GroupSerializer

    success_message = _("Group created successfully")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["form_title"] = _("Create Group")
        kwargs["nested_forms"] = [
            {
                "form": ContextForm(),
                "title": _("Extend information"),
            }
        ]
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("auth:group-list")

    def form_valid(self, form):
        object = form.save()  # noqa
        context_form = ContextForm(
            self.request.POST, self.request.FILES, instance=object.context
        )
        if context_form.is_valid():
            context_form.save()
        else:
            object.delete()
            return super().form_invalid(context_form)
        return super().form_valid(form)


group_create_view = GroupCreateView.as_view()


class GroupUpdateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, UpdateView):
    template_name = "app/update.html"
    model = Group

    form_class = GroupForm
    serializer_class = GroupSerializer
    success_message = _("Group successfully updated")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)

        if self.request.method == "POST":
            context_form = ContextForm(
                self.request.POST, self.request.FILES, instance=self.object.context
            )
        else:
            context_form = ContextForm(instance=self.object.context)
        kwargs["nested_forms"] = [
            {
                "form": context_form,
                "title": _("Extend information"),
            }
        ]
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("auth:group-list")

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = self.get_object()  # noqa
        context_form = ContextForm(
            self.request.POST, self.request.FILES, instance=self.object.context
        )
        form = self.get_form()
        if form.is_valid():
            if context_form.is_valid():
                self.form_valid(context_form)
                return self.form_valid(form)
        messages.error(request, _("Context has error"))
        return self.form_invalid(form)


group_update_view = GroupUpdateView.as_view()
