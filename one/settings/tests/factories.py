from factory import Faker
from factory.django import DjangoModelFactory

from one.settings.models import Setting


class SettingFactory(DjangoModelFactory):
    name = Faker("name")
    main_logo = "/logos/logo-1-dark.svg"

    class Meta:
        model = Setting
        django_get_or_create = ["name"]
