# Generated by Django 5.0 on 2024-11-24 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_rename_tomato_plant_type_category_headertext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='categoryimage',
        ),
    ]
