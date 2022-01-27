def user_avatar_directory_path(instance, filename):
    """Avatar upload path"""
    return "user_{0}/avatar/{1}".format(instance.id, filename)
