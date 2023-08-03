import os
from pathlib import Path

from dotenv import load_dotenv

from root import celery

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET')

DEBUG = True

ALLOWED_HOSTS = ['didocinema.uz']
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    # My Apps
    'apps.movies',
    'apps.users',
    'apps.shared',
    'apps.site_info',

    # Third party apps
    'django_elasticsearch_dsl',
    'storages',
    'django_filters',

]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',   # закомментированно из-за плеера
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
        'DIRS': [BASE_DIR / '../frontend'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'templatehelpers': 'root.templatetags.templatehelpers',

            }
        },
    },
]

WSGI_APPLICATION = 'root.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('SQL_ENGINE'),
        'NAME': os.getenv('SQL_DATABASE'),
        'USER': os.getenv('SQL_USER'),
        'PASSWORD': os.getenv('SQL_PASSWORD'),
        'HOST': os.getenv('SQL_HOST'),
        'PORT': os.getenv('SQL_PORT'),
    }
}

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

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

AUTH_USER_MODEL = 'users.User'

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "../static",
]
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')

CELERY_BROKER_URL = f'amqp://{os.getenv("RABBITMQ_USER")}:{os.getenv("RABBITMQ_PASSWORD")}@localhost:5672/'

CELERY_TIMEZONE = 'Asia/Tashkent'
CELERY_ENABLE_UTC = False

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_ACCESS_KEY_ID = os.getenv("MINIO_ROOT_USER")
AWS_SECRET_ACCESS_KEY = os.getenv("MINIO_ROOT_PASSWORD")
AWS_STORAGE_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.getenv("MINIO_END_POINT")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'django_file': {
            'level': 'INFO',  # Set the desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '../django.log'),  # Path to your log file
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_file'],
            'level': 'DEBUG',  # Set the desired log level for the 'django' logger
            'propagate': False,
        },
    },
}
