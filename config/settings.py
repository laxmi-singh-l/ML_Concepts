"""
Django settings for ml_concepts project.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-dev-key-change-in-production')

DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'ml_libraries',
    'graphs',
    'pandas_numpy',
    'ml_models',
    'testing',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

LEARNING_MODULES = [
    {'id': 1, 'slug': 'libraries', 'name': 'ML Libraries & Setup', 'app': 'ml_libraries', 'icon': 'cpu',
     'description': 'Compare and install scikit-learn, TensorFlow, PyTorch, XGBoost and more'},
    {'id': 2, 'slug': 'data', 'name': 'Data Mastery (Pandas/NumPy)', 'app': 'pandas_numpy', 'icon': 'table',
     'description': 'Learn Pandas and NumPy functions with examples and test code'},
    {'id': 3, 'slug': 'visualization', 'name': 'Visualization Lab', 'app': 'graphs', 'icon': 'graph-up',
     'description': 'Build charts with live preview and get the exact code'},
    {'id': 4, 'slug': 'models', 'name': 'Model Catalog', 'app': 'ml_models', 'icon': 'diagram-3',
     'description': '30+ ML models with starter code and hyperparameter guides'},
    {'id': 5, 'slug': 'training', 'name': 'Training Pipeline', 'app': 'ml_libraries', 'icon': 'play-circle',
     'description': 'Step-by-step pipeline builder with code for each stage'},
    {'id': 6, 'slug': 'evaluation', 'name': 'Evaluation & Testing', 'app': 'testing', 'icon': 'check-circle',
     'description': 'Test generators, metric library, and validation patterns'},
]