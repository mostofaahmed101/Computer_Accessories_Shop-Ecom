# 🖥️ Computer Accessories Shop – Django E-commerce Website

A fully functional and secure **eCommerce website** built with **Python Django**. This project is focused on selling computer accessories like keyboards, mice, cables, and more. It comes with essential eCommerce features including user login, order tracking, invoice generation, admin management, and more.

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Security](https://img.shields.io/badge/security-focused-critical)

---

## 📦 Features

- 🔐 User **Login / Signup** system
- ✅ **Authentication & Authorization** (admin vs user roles)
- 🛒 **Cart** management system
- 💳 **Demo payment simulation**
- 🧾 **PDF Invoice** download (via `xhtml2pdf`)
- 🗃️ **Admin panel** (product, order, user control)
- 📦 **Order tracking** by users
- 📝 **User profile** with update option
- ⭐ **Product feedback** system
- 📄 **Product details** page with full info
- 🎨 Clean, responsive **UI/UX**
- 🔐 Security best practices applied

---

## ⚙️ Technology Stack

| Component       | Details                      |
|----------------|------------------------------|
| Language        | Python 3                     |
| Framework       | Django 3.0.5                 |
| Frontend        | HTML5, CSS3, Bootstrap       |
| Database        | SQLite (default for dev)     |
| Template Engine | Django Template Language     |
| PDF Generation  | xhtml2pdf                    |

---

## 🛠 Installation & Setup

### ✅ Prerequisites

- Python 3.12+
- `pip` package manager
- Git (optional)
- virtualenv (optional but recommended)

### 📦 Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mostofaahmed101/Computer_Accessories_Shop-Ecom.git
   cd Computer_Accessories_Shop-Ecom
   ```
2. **(Optional) Create virtual environment**

    ```bash
    python -m venv venv
    ```
3. **(Optional) activate virtual environment**

    ```bash
    source venv/bin/activate  # macOS/Linux
    venv/Scripts/activate     # Windows
    ```
4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
5. **Apply database migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. **Create a superuser for the admin panel**

    ```bash
    python manage.py createsuperuser
    ```
7. **Run the development server**

    ```bash
    python manage.py runserver
    ```

### 🔑 UI and Admin Panel
1. Browser : http://127.0.0.1:8000/
2. Admin URL: http://127.0.0.1:8000/admin/
3. Login Admin using the superuser credentials you created.

---

## 🔐 Security Features
This project emphasizes basic security best practices:
1. Django’s built-in authentication system (hashed passwords)
2. CSRF protection on forms
3. Role-based access control for admin operations
4. Input sanitization and validation
5. Secure PDF generation

---

## 💬 Feedback & Support
Follow me for more information, take a look at my other projects <br>
**Website:** https://sites.google.com/view/mostofaahmed-official <br>
**Github:** https://github.com/mostofaahmed101

