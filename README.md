# 🚗 Uber Intelligent Ride Platform

A real-world inspired ride-hailing backend built with **Python, FastAPI, Microservices, PostgreSQL, Docker, Machine Learning, and AI**.

---

# 📈 Current Development Progress

## 🏗️ Project Foundation

- [x] GitHub repository and project structure
- [x] Python virtual environment
- [x] `.gitignore`
- [x] README
- [x] Initial GitHub push

---

# 🔐 Authentication Service

**Swagger:** http://127.0.0.1:8000/docs

### Authentication Setup

- [x] FastAPI & Uvicorn setup
- [x] `/health` endpoint
- [x] APIRouter
- [x] PostgreSQL & SQLAlchemy
- [x] User model and schemas
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
- [x] Added default `RIDER` role
- [x] Verified RIDER registration through Swagger
- [x] Verified RIDER login with JWT

---

# 🚗 Rider Profile

**Swagger:** http://127.0.0.1:8000/docs

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
- [x] Verified Rider Profile APIs through Swagger

---

# 🚘 Driver Service

**Swagger:** http://127.0.0.1:8001/docs

### Driver Service Setup

- [x] Added Driver Service
- [x] Added Driver folder structure
- [x] Added Driver model
- [x] Created `drivers` table in PostgreSQL
- [x] Created Driver schema
- [x] Created Driver profile routes
- [x] Connected Driver routes to Driver Service
- [x] Tested Driver Service
- [x] Tested Driver profile creation
- [ ] Add JWT authentication to Driver Service
- [ ] Add DRIVER role validation
- [ ] Add driver availability/status
- [ ] Add driver location tracking

---

# 🚕 Ride Service

**Swagger:** http://127.0.0.1:8002/docs

## Ride Service Setup

- [x] Added Ride Service
- [x] Created Ride Service application structure
- [x] Created models, routes, schemas, services, and utils folders
- [x] Added `database.py`
- [x] Added `main.py`
- [x] Created Ride model
- [x] Created Ride schema
- [x] Started Ride Service on port `8002`
- [x] Verified Swagger documentation
- [x] Created `rides` table
- [x] Connected Ride Service to PostgreSQL

## Ride APIs

- [x] Implemented `POST /rides/`
- [x] Tested ride creation successfully
- [x] Verified ride creation response
- [x] Implemented `GET /rides/`
- [x] Implemented `GET /rides/{ride_id}`
- [x] Tested ride retrieval by ID
- [x] Verified ride records in PostgreSQL
- [x] Implemented `PATCH /rides/{ride_id}/status`
- [x] Created `RideStatusUpdate` schema
- [x] Added ride status validation using Pydantic
- [x] Added ride status transition validation
- [x] Tested valid ride status transitions
- [x] Tested invalid ride status transitions
- [x] Verified invalid transitions return HTTP `400`
- [x] Verified successful status updates return HTTP `200`


----

# 🌐 API Gateway

**Technology:** NGINX  
**Gateway Port:** `9000`

## API Gateway Development Process

### 1. NGINX Installation

- [x] Downloaded and installed NGINX
- [x] Located NGINX installation
- [x] Verified `nginx.exe`
- [x] Verified NGINX configuration

### 2. Gateway Configuration

- [x] Created NGINX API Gateway configuration
- [x] Configured gateway to listen on port `9000`
- [x] Configured backend service upstreams

----

## Matching Service Setup



**Swagger:** http://127.0.0.1:8004/docs

- [x] Added Matching Service
- [x] Created Matching Service application structure
- [x] Created `app/` directory
- [x] Added `__init__.py`
- [x] Added FastAPI `main.py`


## Matching Service APIs

- [x] Implemented `GET /health`
- [x] Tested health check successfully



By Mukesh Kumar
