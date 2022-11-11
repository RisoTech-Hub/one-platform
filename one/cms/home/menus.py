from django.urls import reverse

from one.cms.home.apps import HomeConfig
from one.core.menu import Menu

Menu.add_item(
    f"{HomeConfig.name}.list",
    {
        "url": reverse("cmshome:cmshome-list"),
        "title": "CMS Home",
        "order": 1,
        "icon": "fa fa-home",
    },
)
