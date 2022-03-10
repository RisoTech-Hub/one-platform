from django.db.models import BooleanField, CharField, SlugField, TextField
from django.utils.translation import gettext_lazy as _

from one.components.models import LingualModel


class Page(LingualModel):
    """
    Page

    name: CharField, Specific name for page
    url: SlugField, Url of page
    content: TextField, Page html context
    is_active: BooleanField, only one active at time
    """

    name = CharField(_("Name of page"), max_length=1000, blank=True, null=True)
    url = SlugField(_("URL of page"), max_length=500, blank=True, null=True)
    is_active = BooleanField(_("Is active"), default=False)
    content = TextField(_("Page html context"))

    def activated(self):
        """
        Activate this instance then deactivate everything else
        :return:
        """
        Page.objects.filter(language=self.language, url=self.url).update(
            is_active=False
        )
        self.is_active = True
        self.save()
