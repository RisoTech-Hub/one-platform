from django.apps import AppConfig


class ComponentsConfig(AppConfig):
    name = "one.components"
    verbose_name = "Components"

    def ready(self):
        pass
