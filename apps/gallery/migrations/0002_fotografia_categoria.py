# Generated by Django 4.1 on 2024-01-21 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('GALAXIA', 'Galaxia'), ('PLANETA', 'Planeta'), ('ESTRELA', 'Estrela')], default='', max_length=100),
        ),
    ]
