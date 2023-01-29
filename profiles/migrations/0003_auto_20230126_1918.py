# Generated by Django 3.2.15 on 2023-01-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default=18),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]