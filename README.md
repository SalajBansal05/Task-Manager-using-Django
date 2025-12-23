# Task-Manager-using-Django
This is a learning-focused Django project that implements a basic task management
application with user authentication.

The project was built incrementally, starting from a simple authentication system
and extending it into a task manager to understand Django backend concepts such as
views, templates, models, and HTTP request handling.

---

## Features

- User authentication (signup, login, logout)
- Per-user task isolation
- Create, edit, and delete tasks
- Mark tasks as completed or pending
- Keep track of completion dates and optional deadlines for tasks
- Filter tasks by status (all / pending / completed)

---

## Tech Stack

- Backend: Django
- Database: SQLite (default Django setup)
- Frontend: Django Templates (basic HTML)
- Authentication: Django built-in auth system

---

## Project Structure (High Level)

- `accounts/`
  - Handles authentication and task-related functionality
  - Contains models, views, and app-specific URLs
  - Includes templates under `templates/accounts/`

- `accounts/models.py`
  - Defines the Task model and its relationship with the User model

- `accounts/views.py`
  - Contains view logic for authentication and task CRUD operations

- `accounts/urls.py`
  - Defines routes related to tasks and authentication

- `todo_app/`
  - Project-level configuration (settings, root URLs, ASGI/WSGI)

- `templates/accounts/`
  - HTML templates for task-related views

- `manage.py`
  - Django management script

---

## Learning Focus

This project was intentionally kept simple on the frontend to focus on:

- Django request–response flow
- URL routing and view design
- Safe data modification using POST requests
- CSRF protection
- User-based access control
- State-dependent fields (e.g. completed vs pending tasks)

---

## Known Limitations & Future Improvements

- UI is minimal and not styled with CSS frameworks
- Form validation is basic and can be improved
- No pagination for large task lists
- No REST API (Django templates only)
- Not intended for production use

These trade-offs were made to prioritize learning backend fundamentals.

---

## Running the Project Locally

1. Clone the repository
2. Create a virtual environment (recommended)
3. Install dependencies
4. Run migrations
5. Start the development server

run in terminal:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
