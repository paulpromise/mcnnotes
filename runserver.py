import os
from notapp.wsgi import application

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notapp.settings')
    execute_from_command_line(['manage.py', 'runserver', os.environ.get('PORT', '8000')])
