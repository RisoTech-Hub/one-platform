from django.db.models import BooleanField, CharField, TextField
from django.utils.translation import ugettext_lazy as _

from one.components.models import LingualModel


class EmailTemplate(LingualModel):
    """
    Email template for reuse

    :var code: CharField, Specific code for core app
    :var subject: CharField, Email title
    :var is_protected: BooleanField, can delete or not
    :var content: TextField, html content
    """

    code = CharField(
        _("Specific code for core app"),
        max_length=50,
        blank=True,
        null=True,
        editable=False,
        unique=True,
    )
    subject = CharField(_("Subject of email"), max_length=1000, blank=True, null=True)
    is_protected = BooleanField(_("Is protected"), default=False)
    content = TextField(_("Html content"))
