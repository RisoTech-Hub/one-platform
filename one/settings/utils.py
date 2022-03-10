def logo_directory_path(instance, filename):
    """Setting Logo upload path"""
    return "settings/{0}/logos/{1}".format(instance.id, filename)
