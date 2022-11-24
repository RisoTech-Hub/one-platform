from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from one.contrib.contenttypes.configs.models import Config


@receiver(post_save, sender=ContentType)
def create_or_update_contenttype_config(sender, instance, **kwargs):
    """This signal creates/updates a Setting object
    after creating/updating a Site object.
    """
    config, created = Config.objects.update_or_create(contenttype=instance)
    if not created:
        config.save()
