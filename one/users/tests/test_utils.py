import pytest

from one.users.models import User
from one.users.utils import user_avatar_directory_path

pytestmark = pytest.mark.django_db


class TestUtils:
    """
    Test utils functions
    """

    def test_user_avatar_directory_path(self, user: User):
        """User avatar directory path"""
        assert (
            user_avatar_directory_path(user, "1.jpg") == f"user_{user.id}/avatar/1.jpg"
        )
