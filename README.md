# 📋 Task Manager

A beginner-friendly Django web application demonstrating core Django concepts through a practical task management system. Built as a learning resource for developers who know basic Python and want to get started with Django web development.

---

## 🌟 Features

- Create, view, edit, and delete tasks
- Set task status — Pending, In Progress, or Done
- Set task priority — Low, Medium, or High
- Assign due dates to tasks
- User registration and login
- Each user sees only their own tasks
- Django Admin panel for data management

---

## ⚙️ Tech Stack

- **Python** 3.12+
- **Django** 5.2 LTS
- **SQLite** — default development database
- **Bootstrap 5** — frontend styling via CDN

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/taskmanager.git
cd taskmanager
```

### 2. Create and activate a virtual environment

```bash
# Create
python -m venv venv

# Activate — Mac / Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin account

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

---

## 📸 Pages

| URL             | Description                                                |
| --------------- | ---------------------------------------------------------- |
| `/`             | Task list — all your tasks with status and priority badges |
| `/<pk>/`        | Task detail — full information for a single task           |
| `/create/`      | Create a new task                                          |
| `/<pk>/edit/`   | Edit an existing task                                      |
| `/<pk>/delete/` | Delete a task with confirmation                            |
| `/login/`       | Login page                                                 |
| `/register/`    | Create a new account                                       |
| `/admin/`       | Django admin panel                                         |

---

## 🧠 Django Concepts Covered

- Models and field types (`CharField`, `TextField`, `DateField`, `ForeignKey`, `choices`)
- Migrations — `makemigrations` and `migrate`
- Function-based views
- URL routing with namespaces and dynamic segments
- Django template language — inheritance, loops, conditions, url tags
- ModelForm — rendering, validation, and saving
- `commit=False` for modifying objects before saving
- CSRF protection
- Django Admin customization
- Built-in authentication — login, logout, registration
- `@login_required` decorator
- Ownership filtering with `request.user`

---

## 🐛 Common Issues

**`no such column: tasks_task.owner`** — Run `python manage.py makemigrations` then `python manage.py migrate`.

**`No module named 'django'`** — Your virtual environment is not activated. Run `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows).

**`TemplateDoesNotExist`** — Make sure `'tasks'` is in `INSTALLED_APPS` inside `settings.py`.

**`403 Forbidden` on form submit** — Add `{% csrf_token %}` inside your `<form>` tag.

---

## 📄 License

Released for educational purposes. Free to use for learning and teaching.

---

<div align="center">
  <sub>Django 5.2 LTS &nbsp;•&nbsp; Python 3.12+</sub>
</div>
