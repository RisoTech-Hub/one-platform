from django.utils.translation import gettext_lazy as _

FORM_TYPE_QUICK = "QUICK_FORM"
FORM_TYPE_FULL = "FULL_FORM"
FORM_TYPE_CHOICES = (
    (FORM_TYPE_QUICK, _("Quick Form")),
    (FORM_TYPE_FULL, _("Full Form")),
)
