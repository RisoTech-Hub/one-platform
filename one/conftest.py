import pytest

from one.settings.models import Setting
from one.settings.tests.factories import SettingFactory
from one.users.models import User
from one.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def setting() -> Setting:
    return SettingFactory()
