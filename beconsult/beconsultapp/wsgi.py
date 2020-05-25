"""
WSGI config for Agruppa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os,sys

sys.path.append('/opt/beconsult/beconsult/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beconsultapp.settings")

os.environ['DJANGO_SETTINGS_MODULE'] ="beconsultapp.settings"

os.environ.setdefault("LANG","en_US.UTF-8")
os.environ.setdefault("LC_ALL","en_US.UTF-8")


application = get_wsgi_application()
