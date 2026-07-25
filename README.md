# Job Application Tracker

A Django-based web app to track job applications, built with Forms, CRUD
operations, Template Inheritance, and Custom Middleware.

## Features
- Home dashboard with total applications and status-wise counts
- Full CRUD for job applications (Create, Read, Update, Delete)
- Delete confirmation page
- Detail page for each application
- Django ModelForm with custom validation:
  - Company name required
  - Position required
  - Salary cannot be negative
  - Deadline cannot be earlier than application date
  - Notes max 500 characters
- Template inheritance with base.html, navbar.html, footer.html
- Bootstrap 5 styling
- Success messages after Create/Update/Delete
- Custom `RequestLoggerMiddleware` that logs date/time, HTTP method, and
  requested URL path to the console for every request

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # optional, for /admin/
python manage.py runserver
```

Visit http://127.0.0.1:8000/


