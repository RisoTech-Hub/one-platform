import os
from importlib import import_module, util
from pprint import pprint

from django.conf import settings
from django.templatetags.static import static


# Core theme class
class KTTheme:
    # Variables
    mode_switch_enabled = False
    mode_default = "light"

    direction = "ltr"

    html_attributes = {}
    html_classes = {}

    # Keep page level assets
    javascript_files = []
    css_files = []
    vendor_files = []

    @staticmethod
    def init():
        KTTheme.html_attributes = {}
        KTTheme.html_classes = {}

        KTTheme.javascript_files = []
        KTTheme.css_files = []
        KTTheme.vendor_files = []

    @staticmethod
    def get_name():
        # Get product name
        return settings.KT_THEME

    @staticmethod
    def add_html_attribute(scope, name, value):
        # Add HTML attributes by scope
        KTTheme.html_attributes.setdefault(scope, {})
        KTTheme.html_attributes[scope][name] = value

    @staticmethod
    def add_html_attributes(scope, attributes):
        # Add multiple HTML attributes by scope
        KTTheme.html_attributes.setdefault(scope, {})
        for key in attributes:
            KTTheme.html_attributes[scope][key] = attributes[key]

    @staticmethod
    def add_html_class(scope, value):
        # Add HTML class by scope
        KTTheme.html_classes.setdefault(scope, [])
        if value not in KTTheme.html_classes[scope]:
            KTTheme.html_classes[scope].append(value)

    @staticmethod
    def print_html_attributes(scope):
        # Print HTML attributes for the HTML template
        attributes = []
        if scope in KTTheme.html_attributes:
            for key in KTTheme.html_attributes[scope]:
                attributes.append(f'{key}="{KTTheme.html_attributes[scope][key]}"')

        return " ".join(attributes)

    @staticmethod
    def print_html_classes(scope, full=True):
        # Print HTML classes for the HTML template
        if not KTTheme.html_classes:
            return ""

        classes = ""
        if scope in KTTheme.html_classes:
            classes = " ".join(KTTheme.html_classes[scope])

        if full:
            return f'class="{classes}"'
        else:
            return classes

    @staticmethod
    def get_svg_icon(path, class_names="svg-icon", folder="media/icons/"):
        # Get SVG icon content
        # Reference to current folder
        svg = open(str(settings.APPS_DIR) + "/assets/" + folder + path).read()
        output = f'<span class="{class_names}">{svg}</span>'
        return output

    @staticmethod
    def asset(path):
        # Get an assets path in assets folder by path
        return static(path)

    @staticmethod
    def set_mode_switch(flag):
        # Set dark mode enabled status
        KTTheme.mode_switch_enabled = flag

    @staticmethod
    def is_mode_switch_enabled():
        # Check dark mode status
        return KTTheme.mode_switch_enabled

    @staticmethod
    def set_mode_default(mode):
        # Set the mode to dark or light
        KTTheme.mode_default = mode

    @staticmethod
    def get_mode_default():
        # Get current mode
        return KTTheme.mode_default

    @staticmethod
    def set_direction(direction):
        # Set style direction
        KTTheme.direction = direction

    @staticmethod
    def get_direction():
        # Get style direction
        return KTTheme.direction

    @staticmethod
    def is_rtl_direction():
        # Check if style direction is RTL
        return KTTheme.direction.lower() == "rtl"

    @staticmethod
    def extend_css_file_name(path):
        # Extend CSS file name with RTL or dark mode
        if KTTheme.is_rtl_direction():
            path = path.replace(".css", ".rtl.css")

        return path

    @staticmethod
    def include_favicon():
        # Include favicon from settings
        # Use static() to use builtin function for assets folder
        # Refer in _keenthemes/settings.py for STATIC_URL settings
        return static(settings.KT_THEME_ASSETS["favicon"])

    @staticmethod
    def include_fonts():
        # Include the fonts from settings
        content = ""
        for url in settings.KT_THEME_ASSETS["fonts"]:
            content += f'<link rel="stylesheet" href="{url}">'

        return content

    @staticmethod
    def get_global_assets(asset_type):
        # Get the global assets
        files = []
        for file in settings.KT_THEME_ASSETS[asset_type]:
            if asset_type == "css":
                # Modify css file name suffix based on the RTL or dark mode settings
                files.append(KTTheme.extend_css_file_name(file))
            else:
                files.append(file)

        return files

    @staticmethod
    def add_vendors(vendors):
        # Add multiple vendors to the page by name. Refer to settings.KT_THEME_VENDORS
        for value in vendors:
            # Skip duplicate entry
            if value not in KTTheme.vendor_files:
                KTTheme.vendor_files.append(value)

    @staticmethod
    def add_vendor(vendor):
        # Add single vendor to the page by name. Refer to settings.KT_THEME_VENDORS
        # Skip duplicate entry
        if vendor not in KTTheme.vendor_files:
            KTTheme.vendor_files.append(vendor)

    @staticmethod
    def add_javascript_file(file):
        # Add custom javascript file to the page
        # Skip duplicate entry
        if file not in KTTheme.javascript_files:
            KTTheme.javascript_files.append(file)

    @staticmethod
    def add_css_file(file):
        # Add custom CSS file to the page
        # Skip duplicate entry
        if file not in KTTheme.css_files:
            KTTheme.css_files.append(file)

    @staticmethod
    def get_vendors(vendor_type):
        # Get vendor files from settings. Refer to settings.KT_THEME_VENDORS
        files = []
        for vendor in KTTheme.vendor_files:
            # Check if vendor exist in the settings
            if vendor_type in settings.KT_THEME_VENDORS[vendor]:
                # Skip duplicate entry
                if settings.KT_THEME_VENDORS[vendor][vendor_type] not in files:
                    for path in settings.KT_THEME_VENDORS[vendor][vendor_type]:
                        # add static url to local file paths, skip for external urls
                        files.append(KTTheme.add_static(path))

        return files

    @staticmethod
    def set_layout(view, context={}):  # noqa
        # Set the current page layout and init the layout bootstrap file
        KTTheme.html_attributes = {}
        KTTheme.html_classes = {}

        layout = os.path.splitext(view)[0]
        layout = layout.split("/")[0]

        # Get module path
        module = f"extend.metronic.{layout}"

        # Check if the bootstrap file is existed
        if not util.find_spec(module) is None:
            # Auto import and init the default bootstrap.py file from the theme
            KTBootstrap = KTTheme.import_class(
                module, "KTBootstrap{}".format(layout.title().replace("-", ""))
            )
            KTBootstrap.init(context)
        else:
            module = "extend.metronic.bootstrap.default"
            KTBootstrap = KTTheme.import_class(module, "KTBootstrapDefault")
            KTBootstrap.init(context)

        return f"{settings.KT_THEME_LAYOUT_DIR}/{view}"

    @staticmethod
    def import_class(from_module, import_class_name):
        # Import a module by string
        pprint(f"Loading {import_class_name} from {from_module}")
        module = import_module(from_module)
        return getattr(module, import_class_name)

    @staticmethod
    def add_static(path):
        if "//" in path:
            return path
        return KTTheme.asset(path)
