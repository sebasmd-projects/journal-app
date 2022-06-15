import json
from django.core.exceptions import ImproperlyConfigured
from unipath import Path

# Build paths inside the project like this: BASE_DIR.child('subdir') ejm BASE_DIR.child('public','static') is public/static
BASE_DIR = Path(__file__).ancestor(3)

# Read the json global settings file
with open("sensitive_data.json") as f: 
    value = json.loads(f.read())
    
# Get the values from the json file
def get_value(value_title, values=value): 
    try: 
        return values[value_title] 
    except: 
        msg = f"The name of {value_title} doesn't exists"
        raise ImproperlyConfigured(msg)
    

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_value('SECRET_KEY')

# Django Application definition
DJANGO_APPS = ( 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
)

# Third Party Application definition
THIRD_PARTY_APPS = (
    'rest_framework',
    'corsheaders',
    'adminsortable2',
    'import_export',
)

# Local Application definition
LOCAL_APPS = (
    
)

# All Application definition joined
INSTALLED_APPS = INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Principal url configuration
ROOT_URLCONF = 'app_core_journal.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('public','templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application configuration
WSGI_APPLICATION = 'app_core_journal.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = get_value('LANGUAGE_CODE')

TIME_ZONE = get_value('TIME_ZONE')

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = BASE_DIR.child('static')
STATICFILES_DIRS = [BASE_DIR.child('public','static')]

MEDIA_URL = BASE_DIR.child('media')
MEDIA_ROOT = BASE_DIR.child('public','media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
