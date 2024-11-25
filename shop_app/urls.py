from django.urls import path
from .views import header_carousel_images, category_list, product_list,ProductDetailView

urlpatterns = [
    path('header-carousel-images/', header_carousel_images, name='header-carousel-images'),
    path('categories/', category_list, name='category-list'),
    path('products/', product_list, name='product-list'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]
