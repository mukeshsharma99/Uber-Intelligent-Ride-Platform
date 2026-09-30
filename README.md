# 🚗 Uber Intelligent Ride Platform

A real-world inspired ride-hailing backend built with **Python, FastAPI, Microservices, PostgreSQL, Docker, Machine Learning, and AI**.

## 📈 Current Development Progress

### 🏗️ Project Foundation

- [x] GitHub repository & project structure
- [x] Python virtual environment
- [x] `.gitignore` & README
- [x] Initial GitHub push

## 🔐 Authentication Service

**Swagger URL:** `http://127.0.0.1:8000/docs`

* [x] FastAPI & Uvicorn setup
* [x] `/health` endpoint
* [x] APIRouter
* [x] PostgreSQL & SQLAlchemy
* [x] User model & schemas
* [x] User registration
* [x] Argon2 password hashing
* [x] User login
* [x] JWT authentication
* [x] JWT expiration
* [x] Bearer token authentication
* [x] Protected `GET /auth/me`
* [x] Verified authenticated user
* [x] Added user `role` field
* [x] Verified user roles in PostgreSQL
* [x] Added protected `GET /auth/users`
* [x] Tested `/auth/users` with JWT authentication
* [x] Added role selection during registration
* [x] Added default `RIDER` role for registration
* [x] Verified RIDER registration through Swagger UI
* [x] Verified RIDER login with JWT

---

## 🚗 Rider Profile

**Swagger URL:** `http://127.0.0.1:8000/docs`

* [x] Added Rider model
* [x] Added Rider schema
* [x] Added Rider routes
* [x] Connected Rider profile with authenticated user
* [x] Added RIDER role validation
* [x] Created protected `POST /riders/profile`
* [x] Tested rider profile creation with JWT
* [x] Created protected `GET /riders/profile`
* [x] Tested rider profile retrieval with JWT
* [x] Verified Rider data in PostgreSQL
* [x] Verified Rider Profile APIs through Swagger UI

---

## 🚗 Driver Profile

**Swagger URL:** `http://127.0.0.1:8001/docs`

* [x] Added Driver folder
* [x] Added Driver model
* [x] Created `drivers` table in PostgreSQL
* [x] Created Driver schema
* [x] Tested Driver schema
* [x] Created Driver profile routes
* [x] Connected Driver routes to Driver service
* [x] Tested Driver Service

---

## 🚕 Ride Service

**Swagger URL:** `http://127.0.0.1:8002/docs`

### Ride Service Setup

* [x] Added Ride Service folder
* [x] Created Ride Service application structure
* [x] Created models, routes, schemas, services, and utils folders
* [x] Added `database.py`
* [x] Added `main.py`
* [x] Created Ride Model
* [x] Created Ride Schema
* [x] Started Ride Service on port 8002
* [x] Verified Swagger documentation
* [x] Created `rides` database table
* [x] Connected Ride Service to PostgreSQL

-----


### Ride APIs

- [x] Implemented `POST /rides/` endpoint
- [x] Tested ride creation successfully in Swagger
- [x] Verified successful response with ride details

- [x] Implemented `GET /rides/` endpoint
- [x] Implemented `GET /rides/{ride_id}` endpoint
- [x] Tested ride retrieval by ID
- [x] Verified ride records in PostgreSQL

- [x] Implemented `PATCH /rides/{ride_id}/status` endpoint
- [x] Created `RideStatusUpdate` schema
- [x] Added ride status validation using Pydantic
- [x] Added ride status transition validation
- [x] Tested valid ride status transitions in Swagger
- [x] Tested invalid ride status transitions in Swagger
- [x] Verified invalid transitions return HTTP 400
- [x] Verified successful status update returns HTTP 200


----

## 🛠️ Technology Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Argon2
* Docker
* Microservices
* Machine Learning
* Artificial Intelligence
* AWS
* CI/CD


## By Mukesh Kumar