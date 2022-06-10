from .settings_base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

BASE_URL = get_value('BASE_URL')['local']

ALLOWED_HOSTS = get_value('ALLOWED_HOSTS')['local']

CORS_ALLOWED_ORIGINS = get_value('CORS_ALLOWED_ORIGINS')['local']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'CONN_MAX_AGE': get_value('DB_CONN_MAX_AGE'),
        'ENGINE': get_value('ENGINE'),
        'NAME': get_value('NAME'),
        'USER': get_value('USER'),
        'PASSWORD': get_value('PASSWORD'),
        'HOST': get_value('HOST'),
        'PORT': get_value('PORT'),
    }
}

EMAIL_USE_SSL = get_value('EMAIL_USE_SSL')

EMAIL_USE_TLS = get_value('EMAIL_USE_TLS')

EMAIL_BACKEND = get_value('EMAIL_BACKEND')

EMAIL_HOST = get_value('EMAIL_HOST')

EMAIL_PORT = get_value('EMAIL_PORT')

EMAIL_HOST_USER = get_value('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = get_value('EMAIL_HOST_PASSWORD')

DEFAULT_FROM_EMAIL = get_value('DEFAULT_FROM_EMAIL')
