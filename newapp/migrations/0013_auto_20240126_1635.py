# Generated by Django 3.1 on 2024-01-26 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0012_categorymodel_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='category',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='images',
        ),
        migrations.DeleteModel(
            name='CategoryModel',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.DeleteModel(
            name='GalleryImage',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
