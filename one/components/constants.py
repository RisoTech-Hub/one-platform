from django.utils.translation import gettext_lazy as _

FORM_TYPE_POPUP = "POPUP_FORM"
FORM_TYPE_PAGE = "PAGE_FORM"
FORM_TYPE_CHOICES = (
    (FORM_TYPE_POPUP, _("Popup Form")),
    (FORM_TYPE_PAGE, _("Page Form")),
)

TAB_GROUP_HIDDEN = _("TAB-HIDDEN")
TAB_GROUP_GENERAL = _("TAB-GENERAL")
TAB_GROUP_SEO = _("TAB-SEO")
TAB_GROUP_DYNAMIC = _("TAB-DYNAMIC")
