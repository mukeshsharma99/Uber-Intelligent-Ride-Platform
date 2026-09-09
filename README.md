# 🚗 Uber Intelligent Ride Platform

A real-world inspired ride-hailing backend platform built with **Python, FastAPI, Microservices, PostgreSQL, Docker, Machine Learning, and AI**.

## 📈 Current Development Progress

### 🏗️ Project Foundation
- [x] Created GitHub repository
- [x] Created project structure
- [x] Set up Python virtual environment
- [x] Added `.gitignore`
- [x] Created README
- [x] Pushed project to GitHub

### 🔐 Authentication Service
- [x] Created Auth Service
- [x] Set up FastAPI and Uvicorn
- [x] Created `/health` endpoint
- [x] Added APIRouter
- [x] Connected health router
- [x] Tested `/health` with Swagger UI
- [x] Verified `200 OK`

### 👤 User Management
- [x] Created SQLAlchemy `User` model
- [x] Added `id`, `username`, `email`, `password_hash`
- [x] Added unique username constraint
- [x] Added unique email constraint

### 📋 User Schema
- [x] Created `UserCreate` schema
- [x] Created `UserLogin` schema
- [x] Added `EmailStr` validation
- [x] Added password validation

### 🔑 User Registration
- [x] Created `POST /auth/register`
- [x] Added Argon2 password hashing
- [x] Connected registration API to PostgreSQL
- [x] Stored users securely
- [x] Prevented duplicate usernames/emails
- [x] Added `400 Bad Request` handling

### 🗄️ Database
- [x] Set up PostgreSQL with Docker
- [x] Created `uber_db`
- [x] Created `users` table
- [x] Connected SQLAlchemy to PostgreSQL
- [x] Verified user records

### 🔐 Password Security
- [x] Created `utils/security.py`
- [x] Configured `pwdlib`
- [x] Added `hash_password()`
- [x] Added `verify_password()`
- [x] Integrated password verification

### 🔐 User Login
- [x] Created `POST /auth/login`
- [x] Added username lookup
- [x] Added password verification
- [x] Handled invalid credentials
- [x] Tested with Swagger UI
- [x] Verified `200 OK`

### 🔐 JWT Authentication
- [x] Created `utils/jwt.py`
- [x] Installed `python-jose[cryptography]`
- [x] Configured JWT
- [x] Added `HS256` algorithm
- [x] Added token expiration
- [x] Created `create_access_token()`
- [x] Created `decode_access_token()`
- [x] Integrated JWT with login
- [x] Successfully generated access token
- [x] Verified JWT login with `200 OK`

### 🧪 API Testing
- [x] Tested registration with Swagger UI
- [x] Tested login with Swagger UI
- [x] Verified JWT access token generation

### 🚀 Next Task
- [ ] Create JWT authentication dependency
- [ ] Protect API endpoints with Bearer Token
- [ ] Create `GET /auth/me`
- [ ] Verify authenticated user