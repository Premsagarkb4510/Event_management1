# Generated by Django 4.1.7 on 2023-03-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_confirm_password_customer_register_confirm_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=25)),
                ('Password', models.CharField(max_length=10)),
                ('St', models.CharField(max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='customer_log',
        ),
        migrations.DeleteModel(
            name='event_team_log',
        ),
        migrations.RenameField(
            model_name='event_team_reg',
            old_name='contact',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='event_team_reg',
            old_name='email_id',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='event_team_reg',
            old_name='place',
            new_name='Place',
        ),
    ]
