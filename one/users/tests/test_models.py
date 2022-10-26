import datetime

import pytest
from django.conf import settings
from django.core.cache import cache

from one.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"


def test_user_last_seen(user: User):
    """test_user_last_seen"""
    assert not user.last_seen


def test_user_is_online(user: User):
    """test_user_online"""
    assert not user.is_online

    now = datetime.datetime.now()
    cache.set(
        f"seen_{user.username}",
        now,
        settings.USER_LAST_SEEN_TIMEOUT,
    )
    assert user.is_online

    cache.set(
        f"seen_{user.username}",
        now - datetime.timedelta(seconds=500),
        settings.USER_LAST_SEEN_TIMEOUT,
    )
    assert not user.is_online
