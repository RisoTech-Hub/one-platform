from django.utils.translation import gettext_lazy as _

EXCLUDE_FIELDS = ["password"]

FORM_LAYOUT_1_COL = "1COL"
FORM_LAYOUT_2_COL = "2COL"

FORM_LAYOUTS = (
    (FORM_LAYOUT_1_COL, _("One column")),
    (FORM_LAYOUT_2_COL, _("Two column")),
)

CLASS_DANGER = "danger"
CLASS_WARNING = "warning"
CLASS_SUCCESS = "success"
CLASS_INFO = "info"
CLASS_PRIMARY = "primary"
CLASS_DARK = "dark"

CLASS_COLOR = (
    (CLASS_DANGER, _("Red")),
    (CLASS_WARNING, _("Yellow")),
    (CLASS_SUCCESS, _("Green")),
    (CLASS_INFO, _("Purple")),
    (CLASS_PRIMARY, _("Blue")),
    (CLASS_DARK, _("Black")),
)
