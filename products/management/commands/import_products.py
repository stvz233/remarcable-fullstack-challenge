import csv
import os
from decimal import Decimal

from django.core.management.base import BaseCommand

from products.models import Category, Product, Tag


class Command(BaseCommand):
    help = 'Import products from a CSV file into the database (idempotent).'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default=None,
            help='Path to the CSV file. Defaults to products.csv in the project root.',
        )

    def handle(self, *args, **options):
        # Resolve the CSV file path: use the --file argument if provided,
        # otherwise fall back to products.csv in the project root directory.
        if options['file']:
            file_path = options['file']
        else:
            # BASE_DIR is four levels up from this file:
            # commands/ -> management/ -> products/ -> project root
            base_dir = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(os.path.abspath(__file__))
                    )
                )
            )
            file_path = os.path.join(base_dir, 'products.csv')

        if not os.path.exists(file_path):
            self.stderr.write(self.style.ERROR(f'File not found: {file_path}'))
            return

        self.stdout.write(f'Importing products from: {file_path}')
        created_count = 0
        updated_count = 0

        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for item in reader:
                # Get or create the category for this product.
                category_obj, _ = Category.objects.get_or_create(name=item['category'])

                # Use get_or_create to ensure idempotency:
                # running this command multiple times will not create duplicates.
                product, created = Product.objects.get_or_create(
                    name=item['name'],
                    defaults={
                        'description': item['description'],
                        'price': Decimal(item['price']),
                        'category': category_obj,
                    }
                )

                # If the product already exists, update its fields to reflect
                # any changes in the CSV (keeps data in sync on re-runs).
                if not created:
                    product.description = item['description']
                    product.price = Decimal(item['price'])
                    product.category = category_obj
                    product.save()
                    updated_count += 1
                else:
                    created_count += 1

                # Process tags: get or create each tag and associate with the product.
                tag_names = [tag.strip() for tag in item['tags'].split(',')]
                for tag_name in tag_names:
                    if tag_name:
                        tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
                        product.tags.add(tag_obj)

        self.stdout.write(
            self.style.SUCCESS(
                f'Import complete. Created: {created_count}, Updated: {updated_count}.'
            )
        )
