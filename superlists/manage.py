#!/usr/bin/env python
import os
import sys
import argparse

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
    # try:
    #     from django.core.management import execute_from_command_line
    # except ImportError:
    #     # The above import may fail for some other reason. Ensure that the
    #     # issue is really that Django is missing to avoid masking other
    #     # exceptions on Python 2.
    #     try:
    #         import django
    #     except ImportError:
    #         raise ImportError(
    #             "Couldn't import Django. Are you sure it's installed and "
    #             "available on your PYTHONPATH environment variable? Did you "
    #             "forget to activate a virtual environment?"
    #         )
    #     raise
    # execute_from_command_line(sys.argv)
    argv = sys.argv
    cmd = argv[1] if len(argv) > 1 else None
    if cmd in ['test']:  # limit the extra arguments to certain commands
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('--liveserver', default='localhost')
        args, argv = parser.parse_known_args(argv)
        # We can save the argument as an environmental variable, in
        # which case it's to retrieve from within `project.settings`,
        os.environ['liveserver'] = args.liveserver
        # or we can save the variable to settings directly if it
        # won't otherwise be overridden.
        from django.conf import settings
        settings.liveserver = args.liveserver

    from django.core.management import execute_from_command_line

    # parse_known_args strips the extra arguments from argv,
    # so we can safely pass it to Django.
    execute_from_command_line(argv)
