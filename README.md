# Notes Application

A simple, secure, and user-friendly note-taking web application built with Django. This application allows users to create, manage, and organize their personal notes.

## Features

- User Authentication (Register/Login)
- Create, Read, Update, and Delete Notes
- Secure User Data Isolation
- Responsive Web Interface
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
