from django.utils.translation import gettext_lazy as _

FIELD_TYPE_BOOLEANFIELD = "BooleanField"
FIELD_TYPE_CHARFIELD = "CharField"
FIELD_TYPE_DATEFIELD = "DateField"
FIELD_TYPE_DATETIMEFIELD = "DateTimeField"
FIELD_TYPE_DECIMALFIELD = "DecimalField"
FIELD_TYPE_EMAILFIELD = "EmailField"
FIELD_TYPE_FILEFIELD = "FileField"
FIELD_TYPE_FLOATFIELD = "FloatField"
FIELD_TYPE_IMAGEFIELD = "ImageField"
FIELD_TYPE_INTEGERFIELD = "IntegerField"
FIELD_TYPE_SLUGFIELD = "SlugField"
FIELD_TYPE_TEXTFIELD = "TextField"
FIELD_TYPE_TIMEFIELD = "TimeField"

FIELD_TYPE_CHOICES = (
    (FIELD_TYPE_BOOLEANFIELD, _("Boolean Field")),
    (FIELD_TYPE_CHARFIELD, _("Char Field")),
    (FIELD_TYPE_DATEFIELD, _("Date Field")),
    (FIELD_TYPE_DATETIMEFIELD, _("DateTime Field")),
    (FIELD_TYPE_DECIMALFIELD, _("Decimal Field")),
    (FIELD_TYPE_EMAILFIELD, _("Email Field")),
    (FIELD_TYPE_FILEFIELD, _("File Field")),
    (FIELD_TYPE_FLOATFIELD, _("Float Field")),
    (FIELD_TYPE_IMAGEFIELD, _("Image Field")),
    (FIELD_TYPE_INTEGERFIELD, _("Integer Field")),
    (FIELD_TYPE_SLUGFIELD, _("Slug Field")),
    (FIELD_TYPE_TEXTFIELD, _("Text Field")),
    (FIELD_TYPE_TIMEFIELD, _("Time Field")),
)

FIELD_TYPE_DEFAULT_ATTRS = {
    FIELD_TYPE_BOOLEANFIELD: {"type": "boolean"},
    FIELD_TYPE_CHARFIELD: {"type": "string"},
    FIELD_TYPE_DATEFIELD: {"type": "string", "format": "date"},
    FIELD_TYPE_DATETIMEFIELD: {"type": "string", "format": "date-time"},
    FIELD_TYPE_DECIMALFIELD: {"type": "number"},
    FIELD_TYPE_EMAILFIELD: {"type": "string", "format": "email"},
    FIELD_TYPE_FILEFIELD: {"type": "string", "format": "binary"},
    FIELD_TYPE_FLOATFIELD: {"type": "number"},
    FIELD_TYPE_IMAGEFIELD: {"type": "string", "format": "binary"},
    FIELD_TYPE_INTEGERFIELD: {"type": "integer"},
    FIELD_TYPE_SLUGFIELD: {"type": "string"},
    FIELD_TYPE_TEXTFIELD: {"type": "string"},
    FIELD_TYPE_TIMEFIELD: {"type": "string", "format": "time"},
}
