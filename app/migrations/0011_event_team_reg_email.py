# Generated by Django 4.1.7 on 2023-04-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_place_event_team_reg_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_team_reg',
            name='Email',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]