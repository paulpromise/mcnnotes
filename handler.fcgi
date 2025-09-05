import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notapp.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
