from django.db import migrations

from one.components.constants import CLASS_DANGER, CLASS_WARNING, CLASS_SUCCESS


def generate_code_names(actions, apps):
    """
    create list code name
    :param actions:
    :param apps:
    :return:
    """

    code_names = []
    for app in apps:
        for action in actions:
            code_names.append(f"{action}_{app}")
    return code_names


def add_group_forward(apps, schema_editor):
    """Auto create Group"""
    Group = apps.get_model("auth", "Group")
    GroupProfile = apps.get_model("groups", "GroupProfile")
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model("contenttypes", "ContentType")

    group_ctt = ContentType.objects.get_for_model(Group)
    Permission.objects.create(
        name="can get list of group",
        content_type=group_ctt,
        codename="list_group",
    )
    # Admin
    admin = Group.objects.create(name="Administrator")
    GroupProfile.objects.create(group=admin, color=CLASS_DANGER)

    # Staff
    staff = Group.objects.create(name="Staff")
    GroupProfile.objects.create(group=staff, color=CLASS_WARNING)

    # User
    user = Group.objects.create(name="User")
    GroupProfile.objects.create(group=user, color=CLASS_SUCCESS)


def add_group_backward(apps, schema_editor):
    """Delete all Group"""
    Group = apps.get_model("auth", "Group")
    Group.objects.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0001_initial"),
        ("users", "0002_auto_20220215_1227"),
        ("sites", "0004_alter_options_ordering_domain"),
    ]

    operations = [migrations.RunPython(add_group_forward, add_group_backward)]
