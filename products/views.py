from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category, Tag


def product_list(request):
    # retrieves all products from the database, along with their related category and tags,
    # (avoid N+1 query problem)
    products = Product.objects.select_related('category').prefetch_related('tags').all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # retrieves the search query, selected category, 
    # and selected tags from the GET parameters of the request.
    search_query = request.GET.get('search', '').strip()
    category_id = request.GET.get('category', '').strip()
    tag_ids = request.GET.get('tags', '').strip()  # removes leading and trailing whitespace.

    # filter products based on the key words
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )

    if category_id:
        products = products.filter(category_id=category_id)

    # filter products based on the selected tags, 
    # allowing for multiple tag selections by splitting the tag IDs.
    if tag_ids:
        tag_id_list = [int(tid) for tid in tag_ids.split(',') if tid.isdigit()]
        if tag_id_list:
            products = products.filter(tags__id__in=tag_id_list).distinct()

    # prepares the context for rendering the template, including the filtered products,
    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_tags': tag_ids.split(',') if tag_ids else [],
    }

    return render(request, 'products/product_list.html', context)
