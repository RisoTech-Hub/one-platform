from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

from one.components.models import BaseModel, DynamicModel, SEOModel


class CMSHome(SEOModel, DynamicModel, BaseModel):
    name = CharField(max_length=255, verbose_name=_("Name"), null=True, blank=True)

    class Meta:
        verbose_name = "CMS Home"
        verbose_name_plural = "CMS Home"

    def __str__(self):
        return self.title
