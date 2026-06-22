# Citizen Complaint Portal System

A Django-based web application for managing citizen complaints. The system allows users to register, log in, and access a dedicated user dashboard, while administrators have access to an admin dashboard.

## Features
* **User Authentication:** Registration and Login functionality.
* **User Details:** Captures CNIC and Full Name along with standard Django user credentials.
* **Dashboards:** Separate dashboards for Users and Administrators.

## Project Structure
* `complaint_portal/` - Main Django project configuration folder (settings, urls).
* `Dashboard/` - The core application handling user registration, authentication, and dashboard views.

## Installation

1. Ensure you have Python installed.
2. Install the required dependencies (mainly Django).
   ```bash
   pip install django
   ```
3. Run migrations to set up the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

* Access the application via `http://localhost:8000/`.
* Register for a new account at `/register/` providing your Full Name, CNIC, Email, Username, and Password.
* Login at `/login/` to access the User Dashboard.
* The Admin Dashboard is located at `/admin_dashboard/`.
