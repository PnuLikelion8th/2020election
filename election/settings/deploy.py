from .base import *
import json



WSGI_APPLICATION = 'election.wsgi'


CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')
config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())


DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

DB_PW = config_secret_deploy['django']['db']['password']
DB_NAME = config_secret_deploy['django']['db']['name']
DB_USER = config_secret_deploy['django']['db']['user']
DB_HOST = config_secret_deploy['django']['db']['host']

DATABASES = {
                'default': {
                      'ENGINE': 'django.db.backends.postgresql',
                      'NAME': DB_NAME,
                      'USER': DB_USER,
                      'PASSWORD': DB_PW,
                      'HOST': DB_HOST,
                      'PORT': '5432',
                }
}
