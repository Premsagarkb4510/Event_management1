# Generated by Django 4.1.7 on 2023-07-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_event_team_reg_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='event_team_details',
        ),
        migrations.AddField(
            model_name='event_team_reg',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event_team_reg',
            name='logo',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='event_team_reg',
            name='package',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]