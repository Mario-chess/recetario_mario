#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recetario_mario.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recetario.settings")
>>>>>>> ef91fd9b0446cc8dca721399711ac6ef81ee7678

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
