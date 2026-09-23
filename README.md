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

### 🚗 **Rider Profile**

- [x] Added Rider model
- [x] Added Rider schema
- [x] Added Rider routes
- [x] Connected Rider profile with authenticated user
- [x] Added RIDER role validation
- [x] Created protected `POST /riders/profile`
- [x] Tested rider profile creation with JWT
- [x] Created protected `GET /riders/profile`
- [x] Tested rider profile retrieval with JWT
- [x] Verified Rider data in PostgreSQL
- [x] Verified Rider Profile APIs through Swagger UI

### 🚗 **Driver Profile**

- [x] Added Driver folder
- [x] Added Driver model
- [x] Created `drivers` table in PostgreSQL
- [x] Created Driver schema
- [x] Tested Driver schema
- [x] Created Driver profile routes
- [x] Connected Driver routes to Driver service
- [x] Tested Driver Service


### 🚕 **Ride Service**

- [x] Added Ride Service folder
- [x] Created Ride Service application structure
- [x] Added `models` folder
- [x] Added `routes` folder
- [x] Added `schemas` folder
- [x] Added `services` folder
- [x] Added `utils` folder
- [x] Added `database.py`
- [x] Added `main.py`



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


## By -Mukesh kumar   