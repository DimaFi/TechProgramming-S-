# Generated by Django 5.1.3 on 2024-11-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_animalphoto_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalphoto',
            name='photo',
        ),
        migrations.AddField(
            model_name='animalphoto',
            name='photo_url',
            field=models.URLField(default='https://example.com/default.jpg', max_length=500, verbose_name='URL Фото'),
            preserve_default=False,
        ),
    ]
