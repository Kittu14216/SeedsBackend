from rest_framework import serializers
from .models import Category, HeaderCarouselImage, Product



class HeaderCarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderCarouselImage
        fields = ['headerimage', 'alt_text', 'caption', 'order']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'categoryimage', 'description', 'headerText']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.slug', read_only=True)
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'cost', 'category', 'image', 'slug', 'botanical_name', 'variety', 'fruit_color', 'life_cycle', 'taste', 'germination_rate', 'days_to_maturity', 'difficulty_level', 'sunlight_requirement', 'sowing', 'soil', 'watering']  # Include the new image field
