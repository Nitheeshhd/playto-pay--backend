# 🚀 PlayTo Payment Dashboard – Explainer

## 🧠 Problem Understanding

The goal was to build a system that allows users to:

* Add money
* Manage wallet balance
* Request withdrawals
* Track transactions

This simulates a real-world fintech wallet system.

---

## 🏗️ System Architecture

### Backend (Django)

* Django handles authentication, API endpoints, and business logic
* Wallet system designed using relational models:

  * Wallet
  * Transaction
  * Payout

### Frontend

* Built using HTML, CSS, and JavaScript
* Dynamic updates using fetch API

### Payment Integration

* Razorpay used for secure payment flow
* Backend generates order → frontend handles checkout

---

## 💡 Key Design Decisions

### 1. Wallet System

Each user has:

* balance
* held_balance

This ensures:

* Safe withdrawal handling
* Real-world fintech simulation

---

### 2. Transaction Tracking

Every action creates a transaction:

* credit
* debit
* status tracking

---

### 3. Authentication

Used Django built-in auth:

* Secure session handling
* Protected APIs using @login_required

---

### 4. Database Choice

SQLite was used for deployment simplicity and faster setup.

The system is designed to easily switch to PostgreSQL for production scaling.

---

### 5. Payment Flow

* Backend creates Razorpay order
* Frontend opens Razorpay checkout
* On success → wallet updated

---

## ⚙️ Trade-offs

| Decision               | Reason                                   |
| ---------------------- | ---------------------------------------- |
| SQLite over PostgreSQL | Faster deployment under time constraints |
| Basic UI               | Focus on functionality first             |
| No async processing    | Simplicity for MVP                       |

---

## 🚀 What I Would Improve Next

* Add webhook-based payment verification
* Use PostgreSQL for scalability
* Add email notifications
* Improve UI with animations and responsiveness
* Add retry mechanism for failed payments

---

## 📊 Scaling Plan

To scale this system:

* Move to PostgreSQL
* Use Redis for caching
* Add Celery for async tasks
* Deploy using Docker + CI/CD

---

## 🎯 Final Thoughts

This project demonstrates:

* End-to-end product thinking
* Backend + frontend integration
* Real-world payment system design
* Ability to ship under constraints

---

## 👨‍💻 Author

Nitheesh H D
