from django.contrib import admin
from .models import Category, Product, HeaderCarouselImage

# Registering the models with the default admin interface
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(HeaderCarouselImage)




