# Generated by Django 3.1 on 2024-02-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0028_event_details_model_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_mass',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
