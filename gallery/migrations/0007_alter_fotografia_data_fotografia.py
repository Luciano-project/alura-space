# Generated by Django 4.1 on 2024-01-21 22:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_alter_fotografia_data_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
