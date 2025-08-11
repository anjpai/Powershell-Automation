# Powershell-Automation

This is a Django-based project aimed at automating tasks using PowerShell scripts. The application provides a web interface to manage and execute these scripts.

---

## 🛠️ Requirements

- Python 3.8+
- Django 4.x (or compatible version)
- SQLite (default database, included)

---

## 📦 Installation & Setup

1️⃣ **Clone the repository**
```
git clone https://github.com/anjpai/Powershell-Automation.git
cd Powershell-Automation
```

2️⃣ **Create and activate a virtual environment**
```
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3️⃣ **Install dependencies**
```
pip install django
```

4️⃣ **Apply database migrations**
```
python manage.py migrate
```

5️⃣ **Create a superuser (for admin access)**
```
python manage.py createsuperuser
```

6️⃣ **Run the development server**
```
python manage.py runserver
```

7️⃣ **Open in browser**
```
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel
Access the Django Admin at:
```
http://127.0.0.1:8000/admin/
```
Log in with the **superuser credentials** you created earlier.

---

## ⚙️ Usage
- Manage PowerShell automation tasks via the web interface.
- Add, edit, or delete scripts based on your business logic.
- Extend the project by adding:
  - New features
  - Models
  - Templates

---

## 📝 Notes
- Uses **SQLite** by default for simplicity.
- For production, switch to **PostgreSQL** or **MySQL** by updating `settings.py`.
- Add a `.gitignore` file to exclude:
  - `db.sqlite3`
  - `venv/`
  - `__pycache__/`

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🤝 Contribution
- Fork the repository  
- Open issues  
- Submit pull requests  

---

## 📧 Contact
**Created by:** Anjali R Pai
**GitHub:** [anjpai](https://github.com/anjpai)
```

