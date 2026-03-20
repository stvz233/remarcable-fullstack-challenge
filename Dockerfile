FROM python:3.11-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file in the directory into docker /app directory
COPY . /app/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port 10000 for the application
ENV PORT=10000
EXPOSE 10000

CMD python manage.py migrate && python products/management/commands/import_products.py && gunicorn inventory_management.wsgi:application