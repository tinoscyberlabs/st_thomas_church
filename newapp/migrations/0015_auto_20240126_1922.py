# Generated by Django 3.1 on 2024-01-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0014_category_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
