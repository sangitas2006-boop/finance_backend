## Finance Backend System

## About the Project

This is a backend system built using FastAPI to manage financial transactions such as income and expenses.

The goal of this project is to demonstrate clean backend architecture, proper data handling, and structured API design. It allows users to store transactions and retrieve useful insights like total income, expenses, and balance.

---

## Features

* Add new transactions (income/expense)
* View all transactions
* Filter transactions by type or category
* Get financial summary (income, expense, balance)
* Role-based access control (admin, analyst, viewer)

---

## How It Works

* FastAPI handles API routing
* SQLAlchemy manages database interactions
* SQLite is used for storage
* Pydantic validates incoming data

---

## Roles

Roles are passed as query parameters for simplicity:

* **Admin** → Can create transactions
* **Analyst** → Can view summary
* **Viewer** → Can view transactions

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

---

## Project Structure

finance_backend/

├── main.py
├── database.py
├── models.py
├── schemas.py
├── routes/
│   └── transactions.py
├── services/
│   ├── transaction_service.py
│   └── auth_service.py
└── README.md

---

## How to Run

### 1. Create virtual environment

python -m venv venv
venv\Scripts\activate

---

### 2. Install dependencies

pip install fastapi uvicorn sqlalchemy

---

### 3. Run the server

uvicorn main:app --reload

---

### 4. Open API docs

http://127.0.0.1:8000/docs

---

## API Endpoints

### Home

GET / → Check server status

### Transactions

POST /transactions/?role=admin → Create transaction
GET /transactions/?role=viewer → Get all transactions
GET /transactions/filter/?type=income → Filter transactions

### Summary

GET /summary/?role=admin
GET /summary/?role=analyst

---

## Example Request

{
"amount": 500,
"type": "expense",
"category": "food",
"date": "2026-04-03",
"notes": "lunch"
}

---

## Notes

* Role handling is simplified (no authentication system)
* SQLite is used for quick setup
* Focus is on backend design and structure

---

## Trade-offs

* No authentication (JWT/session) to keep scope focused
* No pagination or caching to maintain simplicity

---

## Future Improvements

* Add JWT authentication
* Add pagination & search
* Add unit tests
* Deploy to cloud (Render / Railway)

---

## Final Thoughts

This project focuses on building a clean and maintainable backend rather than adding unnecessary complexity. It demonstrates how to structure APIs, handle data, and implement business logic in a practical way.
