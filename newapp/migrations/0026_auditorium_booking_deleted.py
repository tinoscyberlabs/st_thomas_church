# Generated by Django 3.1 on 2024-02-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0025_auditorium_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditorium_booking',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
