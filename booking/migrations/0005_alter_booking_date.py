# Generated by Django 3.2.15 on 2023-01-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(),
        ),
    ]
