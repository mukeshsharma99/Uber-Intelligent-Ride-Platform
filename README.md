# 🚗 Uber Intelligent Ride Platform

A real-world inspired ride-hailing backend platform built with Python, FastAPI, Microservices, Machine Learning, and AI.

## 📈 Development Progress

### 🏗️ Project Foundation

- [x] Created GitHub repository
- [x] Created project structure
- [x] Set up Python virtual environment
- [x] Added `.gitignore`
- [x] Created initial README
- [x] Pushed project to GitHub

### 🔐 Authentication Service

- [x] Created Auth Service
- [x] Set up FastAPI and Uvicorn
- [x] Created `/health` endpoint
- [x] Created `routes` package
- [x] Created `routes/health.py`
- [x] Added `APIRouter`
- [x] Connected the health router with `main.py`
- [x] Tested `/health` using Swagger UI
- [x] Verified `200 OK` response

### 👤 User Management

- [x] Created `models` package
- [x] Created `models/user.py`
- [x] Created `User` Pydantic model
- [x] Added username, email, and password fields
- [x] Added email validation
- [x] Connected the User model with FastAPI
- [x] Created `POST /auth/register`
- [x] Added password hashing using Argon2
- [x] Tested user registration using Swagger UI
- [x] Verified `200 OK` response

## 🔄 Current Authentication Flow

```text
Client
   ↓
FastAPI
   ↓
POST /auth/register
   ↓
User Model
   ↓
Pydantic Validation
   ↓
Password Hashing
   ↓
Secure Password Hash
   ↓
200 OK