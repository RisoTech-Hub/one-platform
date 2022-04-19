import pytest

from one.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"


def test_user_as_avatar(user: User):
    """test_user_as_avatar"""
    assert "/static/metronic/media/svg/" in user.as_avatar


def test_user_as_name(user: User):
    """test_user_as_name"""
    assert user.as_name is not None


def test_user_as_title(user: User):
    """test_user_as_title"""
    assert user.as_title is not None


def test_user_as_choice(user: User):
    """test_user_as_choice"""
    assert user.as_choice is not None


def test_user_as_cell(user: User):
    """test_user_as_cell"""
    assert user.as_cell is not None


def test_user_as_dict(user: User):
    """test_user_as_dict"""
    assert user.as_dict is not None


def test_update_user(user: User):
    """test_update_user"""
    user.name = "Test"
    user.save()
    assert user.time_modified is not None
