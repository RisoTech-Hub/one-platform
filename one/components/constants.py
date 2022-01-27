from django.utils.translation import gettext_lazy as _

EXCLUDE_FIELDS = ["password"]

FORM_LAYOUT_1_COL = "1COL"
FORM_LAYOUT_2_COL = "2COL"

FORM_LAYOUTS = (
    (FORM_LAYOUT_1_COL, _("One column")),
    (FORM_LAYOUT_2_COL, _("Two column")),
)
