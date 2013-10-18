#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD

=======
>>>>>>> 10c8e5055c2f21162ccbc97b2512916cf0ee7f68
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recetario_mario.settings")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recetario.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
