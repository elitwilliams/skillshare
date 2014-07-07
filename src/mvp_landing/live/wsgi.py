import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mvp_landing.settings'

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
