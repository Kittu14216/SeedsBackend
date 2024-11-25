from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import HeaderCarouselImage, Category, Product
from .serializers import HeaderCarouselImageSerializer, CategorySerializer, ProductSerializer



@api_view(["GET"])
def header_carousel_images(request):
    try:
        images = HeaderCarouselImage.objects.all().order_by('order')
        serializer = HeaderCarouselImageSerializer(images, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(["GET"])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def product_list(request):
    category_slug = request.GET.get('category')
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    else:
        products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug) 
        serializer = ProductSerializer(product) 
        return Response(serializer.data)