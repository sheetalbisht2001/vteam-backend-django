from .env import env
from ddtrace import patch_all; patch_all(logging=True)

SECRET_KEY = env.str('SECRET_KEY')
CLIENT = env.str('CLIENT', 'dev')

DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = '*'

ROOT_URLCONF = 'stractor.urls'
WSGI_APPLICATION = 'stractor.wsgi.application'
ASGI_APPLICATION = 'stractor.routing.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.str('DB_HOST'),
        'PORT': env.int('DB_PORT'),
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'OPTIONS': {
            'sslmode': 'disable',
        }
    }
}

MIGRATION_MODULES = {
    'common': 'db_migrations.common',
}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static_files'

ORDERING_PARAM = 'order'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = [
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Access-Control-Allow-Origin',
]



LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s [%(levelname)s] %(name)s: [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '-  %(message)s'
        }
    },
    'root': {
        'handlers': ['default'],
        'level': 'DEBUG'
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}

