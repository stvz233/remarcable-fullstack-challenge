# remarcable-fullstack-challenge
A full-stack product management system which developed for Remarcable technical assessment. Functionalities include features dynamic search, categorical filtering, and tag indexing using Django's ORM and robust database schema design.

## Live Demo (Recommended)
The application is successfully deployed and live on Render:
**[https://remarcable-fullstack-challenge.onrender.com/](https://remarcable-fullstack-challenge.onrender.com/)**

> **Note on the live demo:** The live deployment uses SQLite with Render's free tier, which has an non-persistent filesystem. This means the database is re-created from `products.csv` on every deployment or service restart. As a result, any data added via the Admin interface on the live demo will not persist across restarts, and the live database is independent from the local development database. For full admin CRUD functionality, please run the project locally following the steps below.

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

### 5. Run Development Server

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`

## Data Population

You don't need to manually add data! I have built an automated tool to handle this:

- **Automatic Import Using CSV Dataset**: Run the following command to load the sample data from `products.csv` into your local database:

```bash
python manage.py import_products
```

- **Manual Import Using Admin**: If you prefer to add products manually, you can use the Django admin interface at `http://127.0.0.1:8000/admin/` (Requires the superuser created in step 4).

## Technical Implementation Highlights
This project is a user-friendly system designed to manage product data efficiently. Here is how I built it:

- **Full-Stack Development**: I used `Django` for the website logic and `Docker` to make sure the app runs the same way on every computer (containerized).
- **Smart Data Loading**: I created a special script called `import_products.py` to upload product information from a CSV file automatically. Even if you run it many times, it won't create duplicate items, keeping the data clean (idempotent).
- **Automatic Online Updates:**: Whenever I update the code on GitHub, the website on Render updates itself automatically. You don’t need to do any manual setup to see the latest version.
- **Reliable Performance**: I fixed several technical pathing issues so the system can find its data files correctly, whether it's running on my laptop or in the cloud.
- **Optimization**: I implemented `select_related` and `prefetch_related` in the `product_list` view to resolve the N+1 query problem, ensuring efficient database interactions.

## Path Definition
- `products/management/commands/`: This was architected with dynamic path resolution to ensure the functions seamlessly across both local development and Docker-based production environments
- `inventory_management/`: The core system configuration directory, managing essential middleware, security settings (including ALLOWED_HOSTS for production), and database routing.
- `products.csv`: The primary data source used for initial product data importing. This is managed through an idempotent import logic to prevent data duplication during CI/CD cycles.

## AI Attribution

Based on the assignment's AI Policy, the following sections involved AI assistance (Gemini & Claude). I declare that I have reviewed and understood all AI-generated code, and all other parts not mentioned specifically below are written independently.

### `products/models.py`
AI was used to suggest the inline comments explaining each model class, field choice, and `Meta` configuration.

### `products/views.py`
The `Q` object pattern for combining `name` and `description` search was AI-suggested.

### `products/admin.py`
AI helped write the inline comments explaining each `ModelAdmin` option.

### `products/management/commands/import_products.py`
AI was used to refactor this script into a proper Django `BaseCommand` subclass (using `handle()`, `add_arguments()`, `self.stdout.write()`, and `self.style.SUCCESS()`).

### `Dockerfile`
AI suggested updating the `CMD` to invoke the import script via `python manage.py import_products` which was the standard management command pattern instead of running the script file directly.
