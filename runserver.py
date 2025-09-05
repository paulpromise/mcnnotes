import os
from notapp.wsgi import application
from django.core.management import execute_from_command_line

def initialize_app():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notapp.settings')
    execute_from_command_line(['manage.py', 'migrate'])
    from create_superuser import create_superuser
    create_superuser()

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notapp.settings')
    initialize_app()
    execute_from_command_line(['manage.py', 'runserver', os.environ.get('PORT', '8000')])
