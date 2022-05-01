def setting_images_directory_path(instance, filename):
    """Avatar upload path"""
    return "setting_{0}/images/{1}".format(instance.id, filename)
