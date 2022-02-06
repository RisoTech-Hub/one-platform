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

    # Admin
    admin = Group.objects.create(name="Administrator")
    GroupProfile.objects.create(group=admin, color=CLASS_DANGER)

    code_names = generate_code_names(
        ["add", "change", "view", "delete"],
        [
            "permission",
            "group",
            "site",
            "emailaddress",
            "emailconfirmation",
            "socialaccount",
            "socialapp",
            "socialtoken",
            "emailtemplate",
            "user",
            "groupprofile",
        ],
    )
    permissions = Permission.objects.filter(codename__in=code_names).values_list(
        "id", flat=True
    )
    admin.permissions.add(*permissions)

    # Staff
    staff = Group.objects.create(name="Staff")
    GroupProfile.objects.create(group=staff, color=CLASS_WARNING)

    code_names = generate_code_names(
        ["add", "change", "view", "delete"],
        [
            "site",
            "emailaddress",
            "emailconfirmation",
            "socialaccount",
            "socialapp",
            "socialtoken",
            "emailtemplate",
            "user",
        ],
    )
    permissions = Permission.objects.filter(codename__in=code_names).values_list(
        "id", flat=True
    )
    admin.permissions.add(*permissions)

    # User
    user = Group.objects.create(name="User")
    GroupProfile.objects.create(group=user, color=CLASS_SUCCESS)

    code_names = generate_code_names(
        ["add", "change", "view", "delete"],
        [
            "emailaddress",
            "emailconfirmation",
            "socialaccount",
            "socialapp",
            "socialtoken",
            "emailtemplate",
            "user",
        ],
    )
    permissions = Permission.objects.filter(codename__in=code_names).values_list(
        "id", flat=True
    )
    admin.permissions.add(*permissions)


def add_group_backward(apps, schema_editor):
    """Delete all Group"""
    Group = apps.get_model("auth", "Group")
    Group.objects.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0001_initial"),
        ("users", "0003_user_avatar"),
    ]

    operations = [migrations.RunPython(add_group_forward, add_group_backward)]
