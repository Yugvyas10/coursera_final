====================================================================
Little Lemon Restaurant - Back-End Developer Capstone Project
====================================================================

PROJECT TITLE:
Back-end developer capstone project

DESCRIPTION:
A full-featured back-end API and web application built with Django REST Framework (DRF) 
for the Little Lemon restaurant. Connects to MySQL, serves static HTML content, implements 
menu & table booking CRUD APIs, supports user registration & token authentication (Djoser/DRF), 
and includes automated unit tests.

====================================================================
API PATHS FOR PEER REVIEW TESTING:
====================================================================
Static Web App:
http://127.0.0.1:8000/
http://127.0.0.1:8000/restaurant/

User Registration & Authentication (Insomnia / HTTP client):
1. User Registration (POST):
   /auth/users/
   /api/registration/users/
   Payload example:
   {
       "username": "your_username",
       "password": "your_password",
       "email": "user@example.com"
   }

2. Generate Auth Token via Djoser (POST):
   /auth/token/login/
   Payload example:
   {
       "username": "your_username",
       "password": "your_password"
   }
   Response returns: {"auth_token": "<token_string>"}

3. Generate Auth Token via DRF (POST):
   /api-token-auth/
   Payload example:
   {
       "username": "your_username",
       "password": "your_password"
   }
   Response returns: {"token": "<token_string>"}

Menu Items API (Public GET / Authenticated POST/PUT/DELETE):
4. List & Create Menu Items:
   /restaurant/menu/
   /restaurant/menu-items/
   /api/menu/
   /api/menu-items/

5. Single Menu Item (GET / PUT / DELETE):
   /restaurant/menu/1
   /restaurant/menu-items/1
   /api/menu/1
   /api/menu-items/1

Table Booking API (Secured - Requires Token Authentication):
Header required for requests:
Authorization: Token <your_token>

6. List Bookings (GET) & Create Booking (POST):
   /restaurant/booking/tables/
   /api/bookings/tables/
   /api/bookings/

7. Single Booking (GET / PUT / DELETE):
   /restaurant/booking/tables/1/
   /api/bookings/tables/1/

====================================================================
HOW TO RUN THE PROJECT LOCALLY:
====================================================================
1. Clone the repository:
   git clone <repo-url>
   cd <repo-folder>

2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install requirements:
   pip install -r requirements.txt

4. Configure Database:
   - By default, settings.py connects to MySQL database 'LittleLemon':
     Database: LittleLemon
     User: root
     Host: 127.0.0.1
     Port: 3306
   - If MySQL is not running locally, you can use SQLite by setting:
     export USE_SQLITE=1

5. Apply migrations:
   python manage.py migrate

6. Run Unit Tests:
   python manage.py test

7. Run the development server:
   python manage.py runserver

====================================================================
TESTING WITH INSOMNIA REST CLIENT:
====================================================================
1. Create a User:
   - POST to http://127.0.0.1:8000/auth/users/ with JSON payload (username & password).
2. Obtain Token:
   - POST to http://127.0.0.1:8000/api-token-auth/ or /auth/token/login/
   - Copy the generated auth token.
3. Access Menu API:
   - GET http://127.0.0.1:8000/restaurant/menu/
   - POST http://127.0.0.1:8000/restaurant/menu/ with title, price, inventory.
4. Access Secured Booking API:
   - Add Header: 'Authorization': 'Token <your_token>'
   - GET http://127.0.0.1:8000/restaurant/booking/tables/
   - POST http://127.0.0.1:8000/restaurant/booking/tables/ with:
     {
         "name": "Jane Doe",
         "no_of_guests": 4,
         "booking_date": "2026-10-25T19:00:00Z"
     }
