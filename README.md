# 🚗 Uber Intelligent Ride Platform

## 📈 Development Progress

### Day 1 — Project Foundation

* [x] Created GitHub repository
* [x] Created project structure
* [x] Set up Python virtual environment
* [x] Added `.gitignore`
* [x] Created initial README
* [x] Pushed initial project to GitHub

### Day 2 — Auth Service Foundation

* [x] Created Auth Service
* [x] Set up FastAPI and Uvicorn
* [x] Created `/health` endpoint
* [x] Ran the service locally
* [x] Pushed changes to GitHub

### Day 3 — Auth Service Routing

* [x] Created `routes` package
* [x] Created `routes/health.py`
* [x] Added `APIRouter`
* [x] Moved `/health` endpoint to `health.py`
* [x] Connected the health router with `main.py`
* [x] Tested `/health` using Swagger UI
* [x] Verified `200 OK` response
* [ ] Commit and push Day 3 changes

### Day 4 — User Model

* [x] Created `models` package
* [x] Created `models/user.py`
* [x] Added `User` Pydantic model
* [x] Added username, email, and password fields
* [x] Added email validation
* [x] Connected the User model with FastAPI
* [x] Created a temporary `POST /user` endpoint
* [x] Tested `POST /user` using Swagger UI
* [x] Verified `200 OK` response
* [ ] Move user endpoint to `routes/auth.py`
* [ ] Create `POST /auth/register`
* [ ] Add password hashing
* [ ] Commit and push Day 4 changes

### 📍 Current Status

**Day 4 — Auth Service development is in progress.**

Current flow:

```text
Client
  ↓
FastAPI
  ↓
User Model
  ↓
Pydantic Validation
  ↓
POST /user
  ↓
200 OK
```

### 🔜 Next Step

Move the temporary user endpoint into `routes/auth.py` and implement the proper `/auth/register` flow.


### By- Mukesh Kumar