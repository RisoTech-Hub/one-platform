from django.apps import apps


class Menu:
    items = {}
    sorted = {}
    loaded = False

    @classmethod
    def add_item(cls, name, detail):
        """
        add_item adds MenuItems to the menu identified by 'name'
        """
        if name not in cls.items:
            cls.items[name] = detail

    @classmethod
    def load_menus(cls):
        """
        load_menus loops through INSTALLED_APPS and loads the menu.py
        files from them.
        """

        # we don't need to do this more than once
        if cls.loaded:
            return

        # Fetch all installed app names
        app_names = [app_config.name for app_config in apps.get_app_configs()]

        # loop through our INSTALLED_APPS
        for app in app_names:
            # skip any django apps
            if app.startswith("django."):
                continue

            menu_module = "%s.menus" % app
            try:
                __import__(
                    menu_module,
                    fromlist=[
                        "menu",
                    ],
                )
            except ImportError:
                pass

        cls.loaded = True

    @classmethod
    def process(cls):
        # make sure we're loaded
        cls.load_menus()
        return cls.items
