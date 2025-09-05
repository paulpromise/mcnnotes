from django.contrib.auth.models import User
from django.db import IntegrityError

def create_superuser():
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'Admin@123')
            print('Superuser created successfully')
        else:
            print('Superuser already exists')
    except IntegrityError:
        print('Error creating superuser')

if __name__ == '__main__':
    import django
    django.setup()
    create_superuser()
