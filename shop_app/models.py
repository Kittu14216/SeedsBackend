from django.db import models
from django.utils.text import slugify


class HeaderCarouselImage(models.Model):
    headerimage = models.ImageField(upload_to='header_carousel_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.alt_text or f"Image {self.id}"


    def __str__(self):
        return self.alt_text or f"Image {self.id}"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    categoryimage = models.ImageField(upload_to='category_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    headerText = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    botanical_name = models.CharField(max_length=100, blank=True, null=True)
    variety = models.CharField(max_length=100, blank=True, null=True)
    fruit_color = models.CharField(max_length=100, blank=True, null=True)
    life_cycle = models.CharField(max_length=100, blank=True, null=True)
    taste = models.CharField(max_length=100, blank=True, null=True)
    germination_rate = models.CharField(max_length=100, blank=True, null=True)
    days_to_maturity = models.CharField(max_length=100, blank=True, null=True)
    difficulty_level = models.CharField(max_length=100, blank=True, null=True)
    sunlight_requirement = models.TextField(blank=True, null=True)
    sowing = models.TextField(blank=True, null=True)
    soil = models.TextField(blank=True, null=True)
    watering = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
