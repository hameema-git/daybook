from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-secret-key'

DEBUG = False

ALLOWED_HOSTS = ['*','Daybook.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tracker',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'daybook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'daybook.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATIC_ROOT = BASE_DIR / 'staticfiles'  # For collecting static files when deploying
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [BASE_DIR / 'static']  # The location of your static files

PWA_SERVICE_WORKER_PATH = BASE_DIR / 'static/sw.js'

PWA_APP_NAME = 'DayBook'  # The name of your app
PWA_APP_DESCRIPTION = "Track your daily expenses and income"
PWA_APP_THEME_COLOR = '#000000'  # Theme color for the app
PWA_APP_BACKGROUND_COLOR = '#ffffff'  # Background color
PWA_APP_ICONS = [
    {"src": "/static/icons/icon-192x192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "/static/icons/icon-512x512.png", "sizes": "512x512", "type": "image/png"},
]
PWA_APP_DIR = 'ltr'  # Left to Right text direction
PWA_APP_LANG = 'en-US'  # Language of the app
# PWA_SERVICE_WORKER_PATH = 'sw.js'  # Service Worker JavaScript file path
