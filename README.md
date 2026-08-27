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
- [x] Created `routes` package
- [x] Created `routes/health.py`
- [x] Added `APIRouter`
- [x] Connected health router with `main.py`
- [x] Tested `/health` using Swagger UI
- [x] Verified `200 OK` response

### 👤 User Management

- [x] Created `models` package
- [x] Created `models/user.py`
- [x] Created SQLAlchemy `User` model
- [x] Added `id`, `username`, `email`, and `password_hash`
- [x] Added unique username constraint
- [x] Added unique email constraint

### 📋 User Schema

- [x] Created `schemas` package
- [x] Created `schemas/user.py`
- [x] Created `UserCreate` Pydantic schema
- [x] Added username field
- [x] Added email validation using `EmailStr`
- [x] Added password field

### 🔑 User Registration

- [x] Created `POST /auth/register`
- [x] Added Argon2 password hashing
- [x] Added SQLAlchemy database session
- [x] Connected registration API to PostgreSQL
- [x] Successfully stored users in PostgreSQL
- [x] Password stored as a secure hash
- [x] Prevented duplicate usernames
- [x] Prevented duplicate emails
- [x] Added proper `400 Bad Request` responses

### 🗄️ Database

- [x] Set up PostgreSQL using Docker
- [x] Created `uber_db` database
- [x] Created `users` table
- [x] Connected SQLAlchemy with PostgreSQL
- [x] Verified user records using PostgreSQL

### 🧪 API Testing

Registration tested using **FastAPI Swagger UI**.

#### Successful Registration

```json
{
  "username": "mukesh2",
  "email": "mukesh2@example.com",
  "password": "Test@123"
}