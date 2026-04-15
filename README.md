# FastAPI MongoDB JWT Example

This is a FastAPI application with MongoDB integration and JWT-based authentication (access and refresh tokens). Passwords are securely hashed using Argon2.

## Features
- User registration and login
- JWT access and refresh token generation
- All API routes are protected and require authentication
- MongoDB integration for user storage

## Requirements
- Python 3.8+
- MongoDB running locally (default URL: `mongodb://localhost:27017/`)

## Setup

1. **Clone or Download the Repository**

2. **Create and Activate a Virtual Environment**

   ```sh
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On Linux/Mac:
   source env/bin/activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory with the following content:
   ```env
   MONGO_URL=mongodb://localhost:27017/
   SECRET_KEY=your_secret_key_here
   ```

5. **Run MongoDB**
   Ensure MongoDB is running locally on the default port.

6. **Start the Application**

   ```sh
   python run.py
   ```
   or
   ```sh
   uvicorn main:app --reload --host 127.0.0.1 --port 3000
   ```

## API Endpoints

- `POST /register` — Register a new user (username & password)
- `POST /token` — Obtain access and refresh tokens (OAuth2PasswordRequestForm)
- `GET /hello` — Example protected route (requires Authorization header)

## Usage Example

1. **Register a User**
   ```sh
   curl -X POST "http://127.0.0.1:3000/register" -d 'username=alice&password=yourpassword' -H "Content-Type: application/x-www-form-urlencoded"
   ```

2. **Get Tokens**
   ```sh
   curl -X POST "http://127.0.0.1:3000/token" -d 'username=alice&password=yourpassword' -H "Content-Type: application/x-www-form-urlencoded"
   ```

3. **Access Protected Route**
   ```sh
   curl -H "Authorization: Bearer <access_token>" http://127.0.0.1:3000/hello
   ```

## Notes
- Passwords are hashed with Argon2 (no length limit).
- All endpoints except `/register` and `/token` require authentication.
- You can use tools like Postman or httpie for easier API testing.

---

Feel free to extend this application with more features!
