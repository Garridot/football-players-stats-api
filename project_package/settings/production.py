"""
Production environment settings.
"""
from .base import *
import dj_database_url
import os

DEBUG = os.environ.get("DEBUG_PRODUCTION")

ALLOWED_HOSTS_PRODUCTION_VALUE = os.environ.get('ALLOWED_HOSTS_PRODUCTION')

if ALLOWED_HOSTS_PRODUCTION_VALUE:    
    ALLOWED_HOSTS = [s.strip() for s in ALLOWED_HOSTS_PRODUCTION_VALUE.split(',')]
else:    
    ALLOWED_HOSTS = []

# DB_URL = os.environ.get("DATABASE_CONFIG")

# if not DB_URL:    
#     DB_URL = env("DATABASE_CONFIG")

# DATABASES = {
# 	"default": dj_database_url.parse(DB_URL)
# }