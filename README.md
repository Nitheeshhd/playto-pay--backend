# 💳 PlayTo – Smart Payment Dashboard

🌐 **Live Demo:** https://your-render-link.onrender.com
📦 **GitHub Repo:** https://github.com/Nitheeshhd/playto-pay--backend

---

## 🚀 Overview

PlayTo is a **full-stack fintech-style payment dashboard** built using Django.
It allows users to securely manage wallet balance, perform transactions, and simulate real-world payment flows using Razorpay.

This project demonstrates **production-level architecture, secure API handling, and modern UI/UX design**.

---

## ✨ Features

### 🔐 Authentication System

* User Signup & Login
* Session-based authentication
* Secure logout system

### 💰 Wallet Management

* Add money using Razorpay (Test Mode)
* Withdraw money with bank validation
* Real-time balance updates

### 💳 Payment Integration

* Razorpay Checkout integration
* Backend order creation (secure)
* Payment success handling

### 📊 Dashboard & Analytics

* Live wallet balance
* Transaction history
* Credit vs Debit chart (Chart.js)
* Admin analytics dashboard

### 🏦 Payout System

* Account number validation
* IFSC validation
* Held balance system
* Transaction tracking

---

## 🧠 Tech Stack

| Layer    | Technology            |
| -------- | --------------------- |
| Backend  | Django                |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite / PostgreSQL   |
| Payment  | Razorpay API          |
| Charts   | Chart.js              |

---

## 🎨 UI / UX Design

The UI is inspired by modern fintech platforms like:

* Razorpay Dashboard
* Flipkart UI patterns
* Glassmorphism + Gradient-based design

Key UI Features:

* Smooth animations
* Card-based layout
* Responsive design
* Clean dashboard experience

---

## 🔐 Security Practices

* API keys stored using environment variables
* No sensitive data exposed in frontend
* Authentication enforced using `@login_required`
* Secure backend payment handling

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/Nitheeshhd/playto-pay--backend.git
cd playto-pay--backend

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🔑 Environment Variables

Create `.env` file:

```env
RAZORPAY_KEY=rzp_test_xxxxx
RAZORPAY_SECRET=xxxxx
```

---

## 🧪 Demo Credentials

```txt
Username: testuser
Password: test123
```

---

## 💳 Razorpay Test Payment

Use this test card:

```txt
Card Number: 4111 1111 1111 1111
Expiry: Any future date
CVV: 123
OTP: 1234
```

---

## 📊 Admin Dashboard

* Total Users
* Total Transactions
* Total Revenue
* Chart visualization

Access: `/admin-dashboard/`

---

## 🚀 Future Improvements

* Real bank verification (API integration)
* Email notifications
* Mobile responsive UI
* Transaction export (PDF/CSV)

---

## 🎯 What This Project Demonstrates

* Full-stack development
* Payment gateway integration
* Secure backend architecture
* Clean UI/UX design
* Real-world product thinking

---

## 👨‍💻 Author

**Nitheesh H D**
🔗 https://github.com/Nitheeshhd

---

⭐ If you like this project, consider giving it a star!
