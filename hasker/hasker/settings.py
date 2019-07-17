import os
from configurations import Configuration


class Base(Configuration):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    SECRET_KEY = 'ak8+)_h8f7-p*%m8t=3&ia)tz8i76_hyp80is11c-6-lxl=d7-'
    
    ALLOWED_HOSTS = []
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'crispy_forms',
        'forum',
        'authorization',
        '_api',
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
    
    ROOT_URLCONF = 'hasker.urls'
    
    AUTH_USER_MODEL = 'authorization.Person'
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates')
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.template.context_processors.media',
                ],
            },
        },
    ]
    
    WSGI_APPLICATION = 'hasker.wsgi.application'
    
    @property
    def DATABASES(self):
        return {'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(self.BASE_DIR, 'db.sqlite3'),
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
    
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10
    }
    
    EMAIL_HOST = 'smtp.mail.ru'
    EMAIL_PORT = 2525
    EMAIL_HOST_USER = "stereolife@bk.ru"
    EMAIL_HOST_PASSWORD = "live7623"
    EMAIL_USE_TLS = True
    
    LANGUAGE_CODE = 'en-us'
    
    TIME_ZONE = 'UTC'
    
    USE_I18N = True
    
    USE_L10N = True
    
    USE_TZ = True
    
    CRISPY_TEMPLATE_PACK = 'bootstrap4'
    
    LOGIN_URL = '/hasker/auth/login/'
    
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'media')
    
    STATIC_URL = '/static/'
    
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'files', 'static')
    ]


class Local(Base):
    DEBUG = True


class Prod(Base):
    DEBUG = False
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    @property
    def DATABASES(self):
        return {'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(self.BASE_DIR, 'db.sqlite3'),
            }
        }