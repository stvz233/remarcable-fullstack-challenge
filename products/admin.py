from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Product
from import_export.admin import ImportExportModelAdmin

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    # customizes the admin interface for the Category model,
    # allowing users to see the name and description fields, and search by name.
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    # allowing users to see the name field and search by name.
    list_display = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    # allowing users to see the name, category, price, and creation date fields,
    list_display = ['name', 'category', 'price', 'created_at']
    # adds a sidebar filter for category, tags, and creation date to improve navigation
    list_filter = ['category', 'tags', 'created_at']
    # improves discoverability by allowing keyword searches across product names and descriptions.
    search_fields = ['name', 'category__name','description']
    filter_horizontal = ['tags']
    # Displays auto-generated timestamps in the detail view without allowing edits.
    readonly_fields = ['created_at', 'updated_at']