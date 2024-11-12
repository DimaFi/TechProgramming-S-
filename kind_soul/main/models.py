from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image_url = models.URLField(
        max_length=500, blank=True)

    def __str__(self):
        return self.title



class Animal(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мальчик'),
        ('F', 'Девочка')
    ]
    
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Пол")
    photo = models.ImageField(upload_to='animal_photos/', blank=True, null=True, verbose_name="Фото")
    
    def __str__(self):
        return self.name
