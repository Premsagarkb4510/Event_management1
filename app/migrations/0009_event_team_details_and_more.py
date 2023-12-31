# Generated by Django 4.1.7 on 2023-04-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_event_team_reg_license_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_team_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=25)),
                ('district', models.CharField(max_length=10)),
                ('pin', models.IntegerField()),
                ('package', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=30)),
                ('Contact', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('logo', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='event_team_reg',
            old_name='License_id',
            new_name='License_id_number',
        ),
        migrations.RemoveField(
            model_name='event_team_reg',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='event_team_reg',
            name='Package',
        ),
        migrations.RemoveField(
            model_name='event_team_reg',
            name='image',
        ),
        migrations.AddField(
            model_name='event_team_reg',
            name='status',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
