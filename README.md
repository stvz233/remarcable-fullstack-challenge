# remarcable-fullstack-challenge
A full-stack product management system which developed for Remarcable technical assessment. Features dynamic search, categorical filtering, and multi-tag indexing using Django's ORM and robust database schema design.

# Django Product Catalog

## Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

### 2. Install Django

```bash
pip install django
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`

## Data Population

Use the Django admin interface at `http://127.0.0.1:8000/admin/` to populate the database.
