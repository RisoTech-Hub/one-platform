import pytest
from django.urls import resolve, reverse

from one.users.models import User

pytestmark = pytest.mark.django_db


def test_user_detail(user: User):
    assert (
        reverse("api:profile-detail", kwargs={"username": user.username})
        == f"/api/profile/{user.username}/"
    )
    assert resolve(f"/api/profile/{user.username}/").view_name == "api:profile-detail"


def test_user_list():
    assert reverse("api:profile-list") == "/api/profile/"
    assert resolve("/api/profile/").view_name == "api:profile-list"


def test_user_me():
    assert reverse("api:profile-me") == "/api/profile/me/"
    assert resolve("/api/profile/me/").view_name == "api:profile-me"
