import os
from pathlib import Path
from dotenv import load_dotenv

from root import celery

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET')

DEBUG = os.getenv('DJANGO_DEBUG')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps
    'movies.apps.MoviesConfig',
    'users.apps.UsersConfig',
    'shared.apps.SharedConfig'

    # Third party apps

]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',   # закомментировал из-за плеера

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'root.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'film_watch_site',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         },
#         "KEY_PREFIX": "django"
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.users.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.users.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.users.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.users.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

AUTH_USER_MODEL = 'users.User'

USE_TZ = True

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'iamgoodmanbich@gmail.com'
EMAIL_HOST_PASSWORD = 'gkmjsskibpjevnch'

CELERY_BROKER_URL = 'amqp://user:password@localhost/'
