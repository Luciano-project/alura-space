# Generated by Django 4.1 on 2024-01-21 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
