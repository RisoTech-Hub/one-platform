import pytest

from one.settings.models import Setting

pytestmark = pytest.mark.django_db


def test_activated(setting: Setting):
    setting.activated()
    assert setting.is_active is True
