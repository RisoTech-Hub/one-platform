import pytest
from django.contrib.auth.models import Group

from one.auth_extend.contexts.signals import create_or_update_group_context

pytestmark = pytest.mark.django_db


def test_group_context_string(group: Group):
    """test_group_context_string"""
    assert group.context.__str__() == group.name


def test_save_group(group: Group):
    """test_save_group"""
    create_or_update_group_context(Group, group)
    assert group.context.__str__() == group.name
