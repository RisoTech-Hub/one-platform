import pytest
from django.contrib.auth.models import Group

from one.auth_extend.contexts.apps import create_default_group_context
from one.auth_extend.contexts.models import Context

pytestmark = pytest.mark.django_db


def test_create_default_group_context():
    """create_default_group_context"""
    group = Group.objects.create(name="test")
    context = Context.objects.filter(group=group)
    if context.exists():
        context.delete()
    create_default_group_context(())
    assert group.context.__str__() == group.name
