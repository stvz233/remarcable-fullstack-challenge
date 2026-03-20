import django
import os
import csv
from decimal import Decimal

# initialize Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')
django.setup()

from products.models import Product, Category, Tag

def import_products_from_table(file_path):    
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for item in reader:
            category_obj, _ = Category.objects.get_or_create(name=item['category'])

            # get or create the product based on the name, 
            # ensuring idempotency by using get_or_create function.
            product, created = Product.objects.get_or_create(
                name=item['name'],
                defaults={
                    'description': item['description'],
                    'price': Decimal(item['price']),
                    'category': category_obj
                }
            )

            # process tags, ensuring that existing tags are reused and new tags are created as needed.
            tag_names = [tag.strip() for tag in item['tags'].split(',')]
            for tag_name in tag_names:
                tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
                product.tags.add(tag_obj)

            status = "create" if created else "already exists"
            print(f"{status}: {product.name}")

if __name__ == '__main__':
    import_products_from_table('products.csv')