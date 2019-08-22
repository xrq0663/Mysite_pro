from .base import *

DEBUG = False

# 替换成你的域名
ALLOWED_HOSTS = ['www.51xzsx.site', '51xzsx.site']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


