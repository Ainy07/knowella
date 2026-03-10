# 📚 Assignment Projects – Knowella AI Inc.

This repository contains solutions to technical assignments provided by **Knowella AI Inc.** as part of an evaluation process.

The goal of the assignment was to design and implement backend systems demonstrating **system design thinking, scalable architecture, and Python/Django development skills**.
 
--- 

# 📌 Assignment Overview

As part of the technical assessment, the candidate was required to select and complete **three system design problems** from a provided list and implement working solutions.

These projects focus on:

* Backend architecture design
* API development
* Data processing
* System simulation
* Real-world scalable system concepts

---

# 🏗️ Repository Structure

```
assignment
│
├── Social
├── car_monitoring_system
└── configurable_data_processor
```

Each project demonstrates a different backend system design scenario.

---

# 🚀 Projects

---

# 1️⃣ Social – Hot Topics System

A backend system that simulates how a social media platform identifies and displays **trending or hot topics** on the main landing page.

### Key Features

* Trending posts detection
* Category based posts
* Hot topics ranking algorithm
* API for retrieving trending posts
* Search functionality

### Architecture

```
                Users
                  │
                  │
             Landing Page
                  │
            Hot Topics API
                  │
        ┌─────────┴─────────┐
        │                   │
     Redis Cache         Search API
        │                   │
        └─────────┬─────────┘
                  │
             Django Backend
                  │
          Trending Algorithm
                  │
               Database
        (Post + Category Tables)
```

---

# 2️⃣ Car Monitoring & OTA Update System

A backend system that simulates cars sending telemetry data to a centralized monitoring service which determines whether **software updates are required**.

### Key Features

* Car telemetry simulation
* Monitoring service logic
* Critical and non-critical update detection
* Update scheduling
* REST APIs for telemetry and update checking

### Architecture

```
                Car Simulator
                      │
                      │
                Telemetry API
             (POST /api/telemetry/)
                      │
                      │
              Telemetry Processing
                      │
        ┌─────────────┴─────────────┐
        │                           │
 Monitoring Logic Engine     Telemetry Database
 (Engine Temp Analysis)      (TelemetryData Table)
        │
        │
   Update Decision Engine
 (Critical / Non-Critical)
        │
        │
        Update Service
        │
        │
      Update Database
        (Update Table)
        │
        │
        Car System
        │
        │
   GET /api/update/?car=id
        │
        │
   Car decides update timing
 (Immediate / Scheduled)
```

---

# 3️⃣ Configurable Data Processor

A flexible backend system designed to process **CSV and Excel files** and perform configurable operations on the data.

### Key Features

* CSV and Excel file processing
* Dynamic configuration-driven operations
* Data transformation
* Database storage or output file generation
* API-based file upload

### Architecture

```
                User Upload
                     │
                     │
                Upload API
                     │
                     │
            File Processing Engine
                     │
        ┌────────────┴────────────┐
        │                         │
   Configuration Parser      Data Transformer
        │                         │
        └────────────┬────────────┘
                     │
               Data Processor
                     │
             ┌───────┴───────┐
             │               │
        Database          Output File
```

---

# ⚙️ Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* Pandas
* Redis (conceptual for caching)

---

# 🎯 Key Concepts Demonstrated

* Backend system architecture
* REST API development
* Data processing pipelines
* Monitoring systems
* Configurable workflows
* Simulation-based systems
* Scalable design thinking

---

# 👩‍💻 Author

**Ainy Gupta**

Backend Developer
Python | Django | REST APIs

GitHub: https://github.com/Ainy07
