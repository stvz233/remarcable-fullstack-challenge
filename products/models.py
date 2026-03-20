from django.db import models

# Create your models here.

# This file defines the data models for the products app, 
# including Category, Tag, and Product.
class Category(models.Model):
    # The Category model represents a product category, 
    # with a unique name and an optional description.
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    # The Meta class defines metadata for the model, 
    # such as the plural name and default ordering.
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    # The Tag model represents a product tag, with a unique name.
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    # The Product model represents a product, with a name, description, price, 
    # and relationships to category and tags.
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering the default ordering by creation date in descending order.
        ordering = ['-created_at']

    def __str__(self):
        return self.name
