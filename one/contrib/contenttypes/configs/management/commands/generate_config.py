from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create config for default content types"

    def handle(self, *args, **kwargs):
        from django.contrib.contenttypes.models import ContentType

        from one.contrib.contenttypes.configs.models import Config

        for content_type in ContentType.objects.all():
            config, created = Config.objects.get_or_create(
                contenttype=content_type, defaults={}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created config for content type "{content_type}"'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Config for content type "{content_type}" already exists'
                    )
                )
