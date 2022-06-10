"""
ASGI config for app_core_journal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os, json

from django.core.exceptions import ImproperlyConfigured
from django.core.asgi import get_asgi_application

with open("sensitive_data.json") as f: 
    value = json.loads(f.read())
     
def get_value(value_title, values=value): 
    try: 
        return values[value_title] 
    except: 
        msg = f"The name of {value_title} doesn't exists"
        raise ImproperlyConfigured(msg)

if get_value("ENVIRONMENT") == "dev":
    print("dev")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_core_journal.settings.settings_dev')

elif get_value("ENVIRONMENT") == "local":
    print("local")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_core_journal.settings.settings_local')

elif get_value("ENVIRONMENT") == "production":
    print("production")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_core_journal.settings.settings_production')

application = get_asgi_application()
