# Generated by Django 4.2 on 2024-05-07 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_region_comuna_alter_inmueble_comuna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]