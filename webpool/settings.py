import  os
from pathlib import Path
from django.contrib import messages


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-p!iik0=bs22kqp*)pl(0mppem9n=owic54p21j*aj*jxd+lvhj'

DEBUG = False

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    # 'myauth',
    # 'contact',
    # 'contact',
]

INSTALLED_APPS += [
    'myauth',
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webpool.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates'],
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

WSGI_APPLICATION = 'webpool.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'logs' / 'data.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "myauth.NewUser"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]


MEDIA_URL = '/media/'


MESSAGE_TAGS = {
    messages.DEBUG : 'alert-info',
    messages.INFO : 'alert-info',
    messages.SUCCESS : 'alert-success',
    messages.WARNING : 'alert-warning',
    messages.ERROR : 'alert-danger',
}

# CELERY_BROKER_URL = "redis://localhost:6379"
# CELERY_RESULT_BACKEND = "redis://localhost:6379"
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_BACKEND = 'django_ses.SESBackend'
# AWS_ACCESS_KEY_ID = 'AKIA2YXVXV2SZ3WLDL7M'
# AWS_SECRET_ACCESS_KEY = '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'

# Account ID: 7403-2347-1013
#

# CRISPY_TEMPLATE_PACK = 'bootstrap4'
# GRAPPELLI_ADMIN_TITLE = "Stemgon Softwares"
# EMAIL_HOST = config('EMAIL_HOST', default='localhost')
# EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
# EMAIL_USE_SSL = config('EMAIL_USE_TLS', default=True, cast=bool)
# DEFAULT_FROM_EMAIL = 'FlexyTuta <admin@mytuta.co.za>'


# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_HOST = 'server145.web-hosting.com'
# EMAIL_HOST_USER = 'admin@stemgon.co.za'
# EMAIL_HOST_PASSWORD = '#Mulalo96'
# DEFAULT_FROM_EMAIL = 'FlexyTuta Team <admin@stemgon.co.za>'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOG_FILE = os.path.join(BASE_DIR, 'logs/stderr.log')

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}


DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_SCALE = 0.5
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True
SITE_ID = 1