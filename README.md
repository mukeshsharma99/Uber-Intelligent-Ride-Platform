# 🚗 Uber Intelligent Ride Platform

A real-world inspired ride-hailing backend built with **Python, FastAPI, Microservices, PostgreSQL, Docker, Machine Learning, and AI**.

## 📈 Current Development Progress

### 🏗️ Project Foundation

-  GitHub repository & project structure
-  Python virtual environment
- `.gitignore` & README
-  Initial GitHub push

---

## 🔐 Authentication Service

**Swagger URL:** `http://127.0.0.1:8000/docs`

-  FastAPI & Uvicorn setup
- `/health` endpoint
-  APIRouter
-  PostgreSQL & SQLAlchemy
-  User model & schemas
-  User registration
-  Argon2 password hashing
-  User login
-  JWT authentication
-  JWT expiration
-  Bearer token authentication
-  Protected `GET /auth/me`
-  Verified authenticated user
-  Added user `role` field
-  Verified user roles in PostgreSQL
-  Added protected `GET /auth/users`
-  Tested `/auth/users` with JWT authentication
-  Added role selection during registration
-  Added default `RIDER` role for registration
-  Verified RIDER registration through Swagger UI
-  Verified RIDER login with JWT

---

## 🚗 Rider Profile

**Swagger URL:** `http://127.0.0.1:8000/docs`

-  Added Rider model
-  Added Rider schema
-  Added Rider routes
-  Connected Rider profile with authenticated user
-  Added RIDER role validation
-  Created protected `POST /riders/profile`
-  Tested rider profile creation with JWT
-  Created protected `GET /riders/profile`
-  Tested rider profile retrieval with JWT
-  Verified Rider data in PostgreSQL
-  Verified Rider Profile APIs through Swagger UI

---

## 🚗 Driver Profile

**Swagger URL:** `http://127.0.0.1:8001/docs`

-  Added Driver folder
-  Added Driver model
-  Created `drivers` table in PostgreSQL
-  Created Driver schema
-  Tested Driver schema
-  Created Driver profile routes
-  Connected Driver routes to Driver service
-  Tested Driver Service

---

## 🚕 Ride Service

**Swagger URL:** `http://127.0.0.1:8002/docs`

### Ride Service Setup

-  Added Ride Service folder
-  Created Ride Service application structure
-  Created models, routes, schemas, services, and utils folders
-  Added `database.py`
-  Added `main.py`
-  Created Ride Model
-  Created Ride Schema
-  Started Ride Service on port 8002
-  Verified Swagger documentation
-  Created `rides` database table
-  Connected Ride Service to PostgreSQL

### Ride APIs

-  Implemented `POST /rides/` endpoint
-  Tested ride creation successfully in Swagger
-  Verified successful response with ride details
-  Implemented `GET /rides/` endpoint
-  Implemented `GET /rides/{ride_id}` endpoint
-  Tested ride retrieval by ID
-  Verified ride records in PostgreSQL
-  Implemented `PATCH /rides/{ride_id}/status` endpoint
-  Created `RideStatusUpdate` schema
-  Added ride status validation using Pydantic
-  Added ride status transition validation
-  Tested valid ride status transitions in Swagger
-  Tested invalid ride status transitions in Swagger
-  Verified invalid transitions return HTTP 400
-  Verified successful status update returns HTTP 200

---

## 🌐 API Gateway

-  Added API Gateway folder
-  Added Nginx API Gateway configuration
