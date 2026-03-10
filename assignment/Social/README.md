# Social Media Hot Topics API

A scalable backend system built with Django REST Framework that powers the **Hot Topics** feature of a social media platform.

The application identifies the **top 20 trending posts** based on engagement metrics like likes, comments, and shares. Users can also **search topics** and **filter posts by category**.

---

# Problem Statement

Design an application for a social media platform where:

- Users can select categories of interest.
- The platform displays **Top 20 trending posts** on the landing page.
- Categories are few but the **user volume is large**.
- Users can **search topics** within categories.
- The system should be **scalable and efficient**.

---

# Features

- Category based posts
- Trending score algorithm
- Hot Topics API (Top 20 trending posts)
- Search posts by keyword
- Filter posts by category
- Redis caching for high traffic
- REST API based architecture
- JSON responses

---

# Technology Stack

- Python
- Django
- Django REST Framework
- SQLite (for development)
- Redis (for caching)

---


---

# Database Design

## Category

| Field | Type |
|-----|-----|
| id | Integer |
| name | CharField |

---

## Post

| Field | Type |
|------|------|
| title | CharField |
| content | TextField |
| category | ForeignKey |
| likes | Integer |
| comments | Integer |
| shares | Integer |
| trending_score | Integer |
| created_at | DateTime |

---

# Trending Algorithm

Trending score is calculated using engagement metrics.
Trending Score =
(likes × 3) +
(comments × 5) +
(shares × 7)




This helps determine the most popular posts.

---

# API Endpoints

## 1 Hot Topics

Returns **top 20 trending posts**
GET /api/hot-topics/1



Example Response:

```json
[
 {
  "title": "AI is changing the world",
  "likes": 200,
  "comments": 50,
  "shares": 30,
  "trending_score": 1060
 }
]

```
## 2 Category Posts

GET /api/posts/?category=Sports

## 3 Search Topics

GET /api/search/?q=AI

## Redis Caching

To handle large user traffic, the Hot Topics API uses Redis caching.

### Benefits:

Faster API responses

Reduced database load

Scalable architecture

Cache Timeout:


300 seconds (5 minutes)

## Architecture Diagram

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

## Installation

## Clone the repository


```git clone https://github.com/Ainy07/knowella.git```


## Move to project directory


```cd social-hot-topics```


## Install dependencies

```pip install -r requirements.txt```


## Run migrations


```python manage.py migrate```


## Run server


```python manage.py runserver```


## Author

Ainy Gupta , 
Backend Developer , 
Python | Django | REST APIs