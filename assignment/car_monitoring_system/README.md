# 🚗 Car Monitoring & OTA Update System

A backend system that simulates cars sending telemetry data to a centralized monitoring service.
The monitoring service analyzes the data and determines whether a **critical or non-critical software update** is required for the car.

This project demonstrates **system design, asynchronous processing concepts, and backend API development using Django and Django REST Framework.**

---

# 📌 Problem Statement

Build a system where multiple cars send telemetry data (speed, engine temperature, battery health) to a **monitoring service**.

The monitoring service:

* Handles a limited number of expensive monitoring operations.
* Determines whether a **software update is required**.
* Sends update information back to the car system.

Cars then decide:

* Apply update **immediately (critical)**
* **Schedule later (non-critical)**

---

# 🏗️ System Architecture

Car Simulator
⬇
Telemetry API
⬇
Telemetry Data Storage
⬇
Monitoring Logic Engine
⬇
Update Decision Engine
⬇
Update Database
⬇
Car checks updates

---

# ⚙️ Technology Stack

* Python
* Django
* Django REST Framework
* SQLite (default database)
* Requests (for simulator)

---

# 📂 Project Structure

```
car_monitoring_system/
│
├── car_monitoring_system/
│   ├── settings.py
│   ├── urls.py
│
├── telemetry/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── tasks.py
│   └── admin.py
│
├── car_simulator.py
├── manage.py
└── README.md
```

---

# 🗄️ Database Models

## Car

Stores car information.

```
vin
model
owner
```

---

## TelemetryData

Stores telemetry sent from cars.

```
car
speed
engine_temp
battery_health
created_at
```

---

## Update

Stores software updates for cars.

```
car
version
update_type (critical / non_critical)
status
created_at
```

---

# 🔌 API Endpoints

## 1️⃣ Send Telemetry Data

POST `/api/telemetry/`

Example Request

```
{
  "car": 1,
  "speed": 90,
  "engine_temp": 105,
  "battery_health": 95
}
```

Response

```
{
 "message": "Telemetry received"
}
```

---

## 2️⃣ Check Updates for a Car

GET `/api/update/?car=1`

Example Response

```
[
  {
    "id": 1,
    "car": 1,
    "version": "v2.1",
    "update_type": "critical",
    "status": "pending"
  }
]
```

---

# 🚘 Car Simulator

The simulator mimics a car sending telemetry data to the system.

Example script:

```
python car_simulator.py
```

The simulator sends random telemetry data every 5 seconds.

Example telemetry sent:

```
{
 "car":1,
 "speed":85,
 "engine_temp":102,
 "battery_health":90
}
```

---

# 🧠 Monitoring Logic

The monitoring service analyzes telemetry data.

Example logic:

* If `engine_temp > 100` → **Critical update**
* Otherwise → **Non-critical update**

Critical updates are applied immediately while non-critical updates can be scheduled later.

---

# 🚀 How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/Ainy07/knowella.git
```

---

### 2️⃣ Navigate to the project

```
cd car_monitoring_system
```

---

### 3️⃣ Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

---

### 4️⃣ Install dependencies

```
pip install django djangorestframework requests
```

---

### 5️⃣ Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Create admin user

```
python manage.py createsuperuser
```

---

### 7️⃣ Run the server

```
python manage.py runserver
```

---

### 8️⃣ Run car simulator

Open another terminal:

```
python car_simulator.py
```

---

# 📊 Example Workflow

1️⃣ Car sends telemetry data
2️⃣ System stores telemetry in database
3️⃣ Monitoring engine analyzes the data
4️⃣ Update decision engine determines update type
5️⃣ Update is stored in database
6️⃣ Car checks update API to fetch updates

---

# ⭐ Features

* Telemetry data ingestion
* Monitoring engine simulation
* Critical and non-critical update handling
* Car simulator
* REST APIs
* Database tracking of updates

---

# 📈 Future Improvements

* Redis queue for monitoring requests
* Celery workers for asynchronous processing
* Load balancing for monitoring service
* Real-time WebSocket updates
* Multiple car simulation
* Cloud deployment

---

# 👩‍💻 Author

Ainy Gupta
Backend Developer
Python | Django | REST APIs

GitHub: https://github.com/Ainy07
