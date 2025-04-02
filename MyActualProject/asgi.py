import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the ASGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyActualProject.settings')

# Get the ASGI application
application = get_asgi_application()
