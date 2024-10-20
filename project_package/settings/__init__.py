from .base import *
from .jwt import *
from .static import *

import os

env = os.getenv('DJANGO_ENV')

# Import the environment-specific settings
if env == 'production':
    from .production import *  
elif env == 'development':
    from .development import * 

