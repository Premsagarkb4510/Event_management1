# Generated by Django 4.1.7 on 2023-03-24 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_register',
            name='Contact_number',
        ),
        migrations.RemoveField(
            model_name='customer_register',
            name='Place',
        ),
    ]
