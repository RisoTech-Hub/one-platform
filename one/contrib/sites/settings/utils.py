def site_images_directory_path(instance, filename):
    """Site images directory"""
    return f"site_{instance.id}/images/{filename}"


def setting_images_directory_path(instance, filename):
    """Setting images directory"""
    return f"setting_{instance.site.id}/images/{filename}"
