import os
from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hasker.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

application = get_wsgi_application()



