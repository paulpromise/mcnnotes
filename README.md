# Notes Application

A Django-based notes application that allows users to create, organize, and manage their notes with subjects. Features a modern, responsive interface and secure user authentication.

## Features

- User authentication (register, login, logout)
- Create, edit, and delete notes
- Organize notes by subjects
- Clean, modern interface
- Responsive design
- Pagination for better performance
- Subject-based organization
- Real-time relative timestamps

## Local Development

1. Clone the repository
```bash
git clone https://github.com/paulpromise/mcnnotes.git
cd notapp
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Run the development server
```bash
python manage.py runserver
```

## Deployment to Azure

1. Create an Azure App Service:
   - Runtime stack: Python
   - Operating System: Linux
   - Python version: 3.10 or later

2. Set up a PostgreSQL database in Azure

3. Configure the following environment variables in Azure App Service:
   ```
   DJANGO_DEBUG=False
   DJANGO_SECRET_KEY=your-secret-key
   AZURE_POSTGRESQL_CONNECTIONSTRING=your-connection-string
   AZURE_POSTGRESQL_DATABASE=your-database-name
   AZURE_POSTGRESQL_USER=your-database-user
   AZURE_POSTGRESQL_PASSWORD=your-database-password
   AZURE_POSTGRESQL_HOST=your-database-host
   ```

4. Deploy using Azure CLI or GitHub Actions:
   ```bash
   az webapp up --runtime PYTHON:3.10 --sku B1 --name your-app-name
   ```

5. Run migrations on Azure:
   ```bash
   az webapp ssh
   cd site/wwwroot
   python manage.py migrate
   ```

## Security Features

- CSRF protection enabled
- Secure password hashing
- Session security
- HTTPS redirect in production
- Secure cookie settings
- PostgreSQL SSL mode required
- Environment-based configuration
- Protected static files
- SQLite Database Integration

## Technologies Used

- Python
- Django Web Framework
- SQLite Database
- HTML/CSS
- Bootstrap (for styling)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/paulpromise/mcnnoteapp.git
   cd mcnnoteapp
   ```

2. Install requirements:

   ```bash
   pip install -r requirement.txt
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Visit `http://localhost:8000` in your web browser

## Deployment

This application is configured for deployment on Azure App Service with SQLite database integration.

## Project Structure

- `notes/` - Main application directory containing views, models, and forms
- `templates/` - HTML templates for the application
- `static/` - Static files (CSS, JavaScript)
- `notapp/` - Project settings and configuration

## License

This project is open source and available under the MIT License.

## Author

Created by Paul Promise
