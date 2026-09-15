# 🚗 Uber Intelligent Ride Platform

A real-world inspired ride-hailing backend built with **Python, FastAPI, Microservices, PostgreSQL, Docker, Machine Learning, and AI**.

## 📈 Current Development Progress

### 🏗️ Project Foundation

- [x] GitHub repository & project structure
- [x] Python virtual environment
- [x] `.gitignore` & README
- [x] Initial GitHub push

### 🔐 **Authentication Service**

- [x] FastAPI & Uvicorn setup
- [x] `/health` endpoint
- [x] APIRouter
- [x] PostgreSQL & SQLAlchemy
- [x] User model & schemas
- [x] User registration
- [x] Argon2 password hashing
- [x] User login
- [x] JWT authentication
- [x] JWT expiration
- [x] Bearer token authentication
- [x] Protected `GET /auth/me`
- [x] Verified authenticated user
- [x] Added user `role` field
- [x] Verified user roles in PostgreSQL
- [x] Added protected `GET /auth/users`
- [x] Tested `/auth/users` with JWT authentication
- [x] Added role selection during registration
- [x] Added default `RIDER` role for registration
- [x] Verified RIDER registration through Swagger UI
- [x] Verified RIDER login with JWT
- [x] Created Rider model
- [x] Created Riders database table
- [x] Created Rider schemas
- [x] Added `POST /riders/profile`
- [x] Added RIDER role verification for rider profile
- [x] Linked Rider profile with User
- [x] Tested Rider profile creation through Swagger UI
- [x] Verified Rider profile in PostgreSQL

### 🧪 API Testing

- [x] Registration with Swagger UI
- [x] Login & JWT generation
- [x] Bearer token authorization
- [x] Protected `/auth/me`
- [x] Protected `/auth/users`
- [x] Verified `200 OK`
- [x] Verified authenticated user details
- [x] Verified users and roles through Swagger UI

## 🛠️ Technology Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT
- Argon2
- Docker
- Microservices
- Machine Learning
- AI