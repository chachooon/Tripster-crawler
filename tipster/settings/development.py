from tipster.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '6y5pe7+9$#u_o$hxu*z4myu(n0m&y5ww!*0zam7r2i4l+lw9_c')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME', 'tipsterdb'),
        'USER': os.environ.get('DJANGO_DB_USERNAME', 'tipster'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'Bitnarae13!#'),
        'HOST': os.environ.get('DJANGO_DB_HOST', 'tipsterdb.ccwa8tdvz8m4.ap-northeast-2.rds.amazonaws.com'),
        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}