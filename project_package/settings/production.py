"""
Production environment settings.
"""
from .base import *
import dj_database_url
import os

DEBUG = env("DEBUG_PRODUCTION")

# Retrieve the value of ALLOWED_HOSTS_PRODUCTION from .env file
ALLOWED_HOSTS_PRODUCTION = env('ALLOWED_HOSTS_PRODUCTION', default='', cast=lambda v: [s.strip() for s in v.split(',')])
# Set ALLOWED_HOSTS using the retrieved value
ALLOWED_HOSTS = ALLOWED_HOSTS_PRODUCTION

DB_URL = os.environ.get("DATABASE_CONFIG")

if not DB_URL:    
    DB_URL = env("DATABASE_CONFIG")

DATABASES = {
	"default": dj_database_url.parse(DB_URL)
}