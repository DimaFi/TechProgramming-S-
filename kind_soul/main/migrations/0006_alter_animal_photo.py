# Generated by Django 5.1.3 on 2024-11-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_animal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/main/animal_photos/', verbose_name='Фото'),
        ),
    ]
