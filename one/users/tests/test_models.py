import datetime

import pytest
from django.conf import settings
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from one.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/~profile/{user.username}/"


def test_user_display_name_html(user: User):

    assert user.display_name_html == user.name

    user.name = None
    assert user.display_name_html == user.username


def test_user_display_level_html(user: User):
    user.is_superuser = True
    assert (
        user.display_level_html
        == f"""
                <span class='badge badge-light-danger fw-bolder fs-8 px-2 py-1
                '>{_("Super User")}</span>
            """
    )

    user.is_superuser = False
    user.is_staff = True
    assert (
        user.display_level_html
        == f"""
                <span class='badge badge-light-warning fw-bolder fs-8 px-2 py-1
                '>{_("Staff")}</span>
            """
    )

    user.is_superuser = False
    user.is_staff = False
    assert (
        user.display_level_html
        == f"""
                <span class='badge badge-light-info fw-bolder fs-8 px-2 py-1
                '>{_("Member")}</span>
            """
    )


def test_user_is_notification_subcribe(user: User):
    assert not user.is_notification_subcribe


def test_user_active_verbose(user: User):

    user.is_active = True
    assert user.active_verbose() == "Active"

    user.is_active = False
    assert user.active_verbose() == "Not Active"


def test_user_last_seen(user: User):
    assert not user.last_seen()


def test_user_online(user: User):
    assert not user.online()

    now = datetime.datetime.now()
    cache.set(
        f"seen_{user.username}",
        now,
        settings.USER_LASTSEEN_TIMEOUT,
    )
    assert user.online()

    cache.set(
        f"seen_{user.username}",
        now - datetime.timedelta(seconds=500),
        settings.USER_LASTSEEN_TIMEOUT,
    )
    assert not user.online()


def test_user_online_verbose(user: User):
    offline = """<div class="position-absolute translate-middle bottom-0 start-100 mb-6 bg-danger rounded-circle
                  border border-4 border-white h-20px w-20px"></div>"""

    assert user.online_dot_verbose() == offline

    now = datetime.datetime.now()
    cache.set(
        f"seen_{user.username}",
        now,
        settings.USER_LASTSEEN_TIMEOUT,
    )
    online = """<div class="position-absolute translate-middle bottom-0 start-100 mb-6 bg-success rounded-circle
                      border border-4 border-white h-20px w-20px"></div>"""

    assert user.online_dot_verbose() == online
