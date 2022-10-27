Metronic Demo 1 comes with 4 main layout options:

Dark Sidebar:

- In "_templates/layout/_bootstrap/default.py" file, under "init" method, uncomment
  KTBootstrapDefault.init_dark_sidebar_layout(context) line and comment out other lines.
- In "_keenthemes/__init__.py" set "default.html" as default layout template.

Light Sidebar:

- In "_templates/layout/_bootstrap/default.py" file, under "init" method, uncomment
  KTBootstrapDefault.init_light_sidebar_layout(context) line and comment out other lines.
- In "_keenthemes/__init__.py" set "default.html" as default layout template.

Dark Header:

- In "_templates/layout/_bootstrap/default.py" file, under "init" method, uncomment
  KTBootstrapDefault.init_dark_header_layout(context) line and comment out other lines.
- In "_keenthemes/__init__.py" set "default_header_layout.html" as default layout template.

Light Header:

- In "_templates/layout/_bootstrap/default.py" file, under "init" method, uncomment
  KTBootstrapDefault.init_light_header_layout(context) line and comment out other lines.
- In "_keenthemes/__init__.py" set "default_header_layout.html" as default layout template.
