import pytest

from one.settings.models import Setting
from one.settings.utils import logo_directory_path

pytestmark = pytest.mark.django_db


class TestSettingUtils:
    """
    Test Settings utils functions
    """

    def test_logo_directory_path(self, setting: Setting):
        """logo directory path"""
        assert (
            logo_directory_path(setting, "1.jpg")
            == f"settings/{setting.id}/logos/1.jpg"
        )
