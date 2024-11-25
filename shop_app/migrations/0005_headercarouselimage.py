# Generated by Django 5.0 on 2024-11-24 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_rename_image_category_categoryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderCarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='header_carousel_images/')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]