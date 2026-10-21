# Little Lemon Restaurant - Meta Back-End Developer Capstone Project

This repository contains the complete capstone project for the **Meta Back-End Developer Professional Certificate** on Coursera.

The project is built using **Django** and the **Django REST Framework (DRF)** to deliver a backend API for table bookings and menu management for the Little Lemon restaurant, complete with user authentication, MySQL integration, static web templates, and unit tests.

---

## Evaluation Criteria Addressed

- [x] **Static HTML content served with Django**: Accessible at `/` and `/restaurant/`.
- [x] **Git Repository**: Initialized with clean commit history, `.gitignore`, and documentation.
- [x] **MySQL Database Connection**: Configured in `littlelemon/settings.py` (with PyMySQL adapter and SQLite fallback flag).
- [x] **Menu & Table Booking APIs**: Full CRUD operations for Menu items and Bookings.
- [x] **User Registration & Authentication**: Token authentication supported via Djoser (`/auth/users/`, `/auth/token/login/`) and DRF (`/api-token-auth/`).
- [x] **Unit Tests**: 8 unit tests covering models, serializers, views, permissions, and templates with 100% pass rate.
- [x] **Insomnia REST Client compatibility**: Standard REST endpoints with JSON payloads and Bearer/Token auth.
- [x] **Readme.txt**: Provided with exact API paths for peer reviewers.

---

## API Endpoints to Test

### 1. Static Website
- `GET http://127.0.0.1:8000/` or `http://127.0.0.1:8000/restaurant/`

### 2. User Registration & Authentication
- **Register New User**: `POST /auth/users/` or `/api/registration/users/`
  ```json
  {
    "username": "reviewer_user",
    "password": "StrongPassword123!",
    "email": "reviewer@example.com"
  }
  ```
- **Login / Obtain Token (Djoser)**: `POST /auth/token/login/`
  ```json
  {
    "username": "reviewer_user",
    "password": "StrongPassword123!"
  }
  ```
- **Obtain Token (DRF)**: `POST /api-token-auth/`
  ```json
  {
    "username": "reviewer_user",
    "password": "StrongPassword123!"
  }
  ```

### 3. Menu API
- **List Menu Items**: `GET /restaurant/menu/` (also `/api/menu/`, `/api/menu-items/`)
- **Create Menu Item**: `POST /restaurant/menu/`
  ```json
  {
    "title": "Lemon Tart",
    "price": "6.50",
    "inventory": 25
  }
  ```
- **Get/Update/Delete Single Item**: `GET` / `PUT` / `DELETE` `/restaurant/menu/{id}`

### 4. Table Booking API (Secured)
> **Note**: Requires header `Authorization: Token <your_token>`

- **List All Bookings**: `GET /restaurant/booking/tables/` (also `/api/bookings/`)
- **Create Booking**: `POST /restaurant/booking/tables/`
  ```json
  {
    "name": "Jane Smith",
    "no_of_guests": 4,
    "booking_date": "2026-10-25T19:30:00Z"
  }
  ```
- **Get/Update/Delete Booking**: `GET` / `PUT` / `DELETE` `/restaurant/booking/tables/{id}/`

---

## Setup Instructions

### 1. Clone & Set Up Virtual Environment
```bash
git clone <repository_url>
cd <repository_folder>
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Database Configuration
By default, `littlelemon/settings.py` connects to MySQL database `LittleLemon`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LittleLemon',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
If you do not have a local MySQL server running, set the environment variable:
```bash
export USE_SQLITE=1
```

### 3. Run Migrations & Tests
```bash
python manage.py migrate
python manage.py test
```

### 4. Start the Server
```bash
python manage.py runserver
```
