from django.utils.translation import gettext_lazy as _

FORM_TYPE_QUICK = "QUICK_FORM"
FORM_TYPE_FULL = "FULL_FORM"
FORM_TYPE_CHOICES = (
    (FORM_TYPE_QUICK, _("Quick Form")),
    (FORM_TYPE_FULL, _("Full Form")),
)

TAB_GROUP_HIDDEN = _("TAB-HIDDEN")
TAB_GROUP_GENERAL = _("TAB-GENERAL")
TAB_GROUP_SEO = _("TAB-SEO")
TAB_GROUP_DYNAMIC = _("TAB-DYNAMIC")
