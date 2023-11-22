from .base import *

DEBUG=env("DEBUG_PRODUCTION",default=False)
# Retrieve the value of ALLOWED_HOSTS_PRODUCTION from .env file
ALLOWED_HOSTS_PRODUCTION = env('ALLOWED_HOSTS_PRODUCTION', default='', cast=lambda v: [s.strip() for s in v.split(',')])
# Set ALLOWED_HOSTS using the retrieved value
ALLOWED_HOSTS = ALLOWED_HOSTS_PRODUCTION
SECRET_KEY = env('SECRET_KEY')



