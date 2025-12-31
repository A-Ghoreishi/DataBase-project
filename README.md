# Online Shop Database Project

## 📌 Project Overview
This project is a **Database Systems final project** that implements an **Online Shop** using:

- **PostgreSQL** as the relational database
- **FastAPI** for backend API development
- **SQLAlchemy ORM** for database interaction

The project covers all required phases, from requirements analysis and data modeling to database implementation and CRUD operations.

---

## 🧩 Project Phases

### Phase 1: Requirements Analysis
The system supports:
- User management
- Product and category management
- Orders and payments
- Shopping carts
- Addresses and relationships between entities

All functional requirements and relationships (1–N, N–N) were identified and documented.

---

### Phase 2: Data Modeling (ER Diagram)
- Entities such as `User`, `Product`, `Category`, `Order`, `Payment`, etc.
- Primary and foreign keys defined
- Referential integrity enforced

---

### Phase 3: ER to Relational Mapping
- Each entity mapped to a relational table
- Proper normalization applied
- Constraints (PK, FK, UNIQUE, CHECK) defined

---

### Phase 4: Database Implementation
- PostgreSQL database created (`online_shop`)
- All tables implemented
- Sample data inserted (13 records per table)
- SQL CRUD operations tested successfully

---

### Phase 5: API Development (FastAPI)
- RESTful API developed using FastAPI
- CRUD operations implemented for:
  - Users
  - Products
- API tested via Swagger UI

---

## 🛠️ Technologies Used
- Python 3.x
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Pydantic

---

## 📂 Project Structure

online-shop-api/
├── app/
│   ├── main.py         
│   ├── db.py          
│   ├── models.py       
│   ├── schemas.py      
│   ├── crud.py        
│   └── __init__.py
│
├── requirements.txt
├── .env
└── README.md


---

## ⚙️ Environment Setup

### 1️⃣ Create Virtual Environment
bash
python -m venv .venv
Windows: .venv\Scripts\activate



### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Configure Environment Variables

Create a .env file in the project root:

DATABASE_URL=postgresql+psycopg2://postgres:PASSWORD@127.0.0.1:5433/online_shop


Replace PASSWORD with your PostgreSQL password.

### ▶️ Run the Application

From the project root directory:

uvicorn app.main:app --reload

## 🌐 API Endpoints

Health Check

GET /health


Swagger UI (API Documentation & Testing)

http://127.0.0.1:8000/docs

Implemented CRUD APIs

/users — Create, Read, Update, Delete users

/products — Create, Read, Update, Delete products

All CRUD operations were tested successfully using Swagger UI.

## 🧪 Testing

Database integrity verified using SQL queries

CRUD operations tested via Swagger UI

Referential constraints enforced at database level

☁️ Note on Neon (Optional)

For users who prefer not to install PostgreSQL locally, this project can also be connected to Neon, a serverless PostgreSQL cloud service.
Only the DATABASE_URL needs to be updated; no code changes are required.

## ✅ Conclusion

This project demonstrates a complete database-driven application, including:

Proper data modeling

Relational database implementation

API-based CRUD operations

Clean architecture and documentation

The project fulfills all requirements of the Database Systems course



