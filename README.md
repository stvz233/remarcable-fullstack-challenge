# remarcable-fullstack-challenge
A full-stack product management system which developed for Remarcable technical assessment. Features dynamic search, categorical filtering, and multi-tag indexing using Django's ORM and robust database schema design.

## Live Demo (Recommended)
The application is successfully deployed and live on Render:
**[https://remarcable-fullstack-challenge.onrender.com/](https://remarcable-fullstack-challenge.onrender.com/)**

## Technical Implementation Highlights
This project is a user-friendly system designed to manage product data efficiently. Here is how I built it:
- **Full-Stack Development**: I used `Django` for the website logic and `Docker` to make sure the app runs the same way on every computer (containerized).
- **Smart Data Loading**: I created a special script called `import_products.py` to upload product information from a CSV file automatically. Even if you run it many times, it won't create duplicate items, keeping the data clean (idempotent).
- **Automatic Online Updates:**: Whenever I update the code on GitHub, the website on Render updates itself automatically. You don’t need to do any manual setup to see the latest version.
- **Reliable Performance**: I fixed several technical pathing issues so the system can find its data files correctly, whether it's running on my laptop or in the cloud.

## Path Definition
- `products/management/commands/`: This was architected with dynamic path resolution to ensure the functions seamlessly across both local development and Docker-based production environments
- `inventory_management/`: The core system configuration directory, managing essential middleware, security settings (including ALLOWED_HOSTS for production), and database routing.
- `products.csv`: The primary data source used for initial product data importing. This is managed through an idempotent import logic to prevent data duplication during CI/CD cycles.

## Browse In Local (Required more steps)

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

You don't need to manually add data! I have built an automated tool to handle this:

- **Automatic Import (Recommended)**: Run the following command to load the sample data from `products.csv` into your local database:

```bash
python products/management/commands/import_products.py
```

- **Manual Import (Optional)**: If you prefer to add products manually, you can use the Django admin interface at `http://127.0.0.1:8000/admin/` (Requires the superuser created in step 4).

