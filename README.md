# remarcable-fullstack-challenge
A full-stack product management system developed for Remarcable technical assessment. Functionalities include features dynamic search, categorical filtering, and tag indexing using Django's ORM and robust database schema design.

## Live Demo (Recommended)
The application is successfully deployed and live on Render:
**[https://remarcable-fullstack-challenge.onrender.com/](https://remarcable-fullstack-challenge.onrender.com/)**

> **Note on the live demo:** The live deployment uses SQLite with Render's free tier, which has a non-persistent filesystem. This means the database is re-created from `products.csv` on every deployment or service restart. As a result, any data added via the Admin interface on the live demo will not persist across restarts, and the live database is independent from the local development database. For full Admin CRUD functionality, please run the project locally following the steps below.

## Local Development Setup

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Import Sample Data

```bash
python manage.py import_products
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`


## Docker Setup (Alternative to Local Development)

### Prerequisites
- Docker installed and running

### Build and Run

Step 1: Build the image
docker build -t remarcable-app .

Step 2: Run the container
docker run -p 8000:10000 remarcable-app


## Data Population

- **Automatic Import Using CSV Dataset**: Run the following command to load the sample data from `products.csv` into your local database:

```bash
python manage.py import_products
```

- **Manual Import Using Admin**: If you prefer to add products manually, you can use the Django admin interface at `http://127.0.0.1:8000/admin/` (Requires the superuser created in step 4).

## Technical Implementation Highlights
This project is a user-friendly system designed to manage product data efficiently. Here is how I built it:

- **Full-Stack Development**: I used `Django` for the website logic and `Docker` to make sure the app runs the same way on every computer (containerized).
- **Smart Data Loading**: I created a special script called `import_products.py` to upload product information from a CSV file automatically. Even if you run it many times, it won't create duplicate items, keeping the data clean (idempotent).
- **Automatic Online Updates**: Whenever I update the code on GitHub, the website on Render updates itself automatically. You don't need to do any manual setup to see the latest version.
- **Reliable Performance**: I fixed several technical pathing issues so the system can find its data files correctly, whether it's running on my laptop or in the cloud.
- **Optimization**: I implemented `select_related` and `prefetch_related` in the `product_list` view to resolve the N+1 query problem, ensuring efficient database interactions.

## AI Attribution

Based on the assignment's AI Policy, the following sections involved AI assistance (Gemini & Claude). I declare that I have reviewed and understood all AI-generated code, and all other parts not mentioned specifically below are written independently.

### `products/views.py`
The `Q` object pattern for combining `name` and `description` search was AI-suggested.

### `products/management/commands/import_products.py`
AI was used to refactor this script into a proper Django `BaseCommand` subclass (using `handle()`, `add_arguments()`, `self.stdout.write()`, and `self.style.SUCCESS()`).

### `inventory_management/settings.py`
AI suggested reading `SECRET_KEY` and `DEBUG` from environment variables via `os.environ.get()` as a security best practice, and making `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` conditional on `DEBUG` to support both local and production environments.

### `Dockerfile`
AI suggested updating the `CMD` to invoke the import script via `python manage.py import_products`, which is the standard management command pattern instead of running the script file directly.

### `products/templates/products/product_list.html`
AI suggested the base CSS styling (layout, card design, color scheme). 
The HTML structure, Django template logic, and JavaScript form handling were written independently.
