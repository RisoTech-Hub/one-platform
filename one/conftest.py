import pytest
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from one.contrib.sites.tests.factories import SiteFactory
from one.extend.riso_auth.tests.factories import GroupFactory
from one.users.models import User
from one.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def site() -> Site:
    return SiteFactory()


@pytest.fixture
def group() -> Group:
    return GroupFactory()
