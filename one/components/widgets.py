from django.forms import Select
from django.forms.widgets import DateInput, Input, SelectMultiple, TextInput


class BootstrapInput(Input):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs["class"] = "form-control"


class SelectTwo(Select):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs, choices)
        self.attrs["class"] = "form-control"
        self.attrs["data-plugin-selectTwo"] = True


class SelectTwoMultiple(SelectTwo, SelectMultiple):
    pass


class ModelSelectTwo(SelectTwo):
    template_name = "widgets/model_select.html"

    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs, choices)
        self.attrs["class"] = "custom-select"


class ModelSelectTwoMultiple(ModelSelectTwo, SelectMultiple):
    pass


class UniqueTextWidget(TextInput):
    template_name = "widgets/unique_text.html"

    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs["class"] = "form-control"


class SpanDateInput(DateInput):
    template_name = "widgets/date_input.html"

    def __init__(self, attrs=None, format=None):  # noqa
        super().__init__(attrs, format)
        self.attrs["class"] = "form-control"
        self.attrs["data-plugin-datepicker"] = ""
        self.attrs["data-date-format"] = "dd/mm/yyyy"
