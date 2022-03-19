from django.contrib.auth.mixins import LoginRequiredMixin

from one.components.views import ExposeListView
from one.emails.models import EmailTemplate


class EmailTemplateListView(LoginRequiredMixin, ExposeListView):
    model = EmailTemplate


email_template_list_view = EmailTemplateListView.as_view()
