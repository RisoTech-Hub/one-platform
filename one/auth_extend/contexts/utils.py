def group_images_directory_path(instance, filename):
    """Group images directory"""
    return f"group_{instance.id}/images/{filename}"


def group_context_images_directory_path(instance, filename):
    """Group context images directory"""
    return f"group_context_{instance.group.id}/images/{filename}"
