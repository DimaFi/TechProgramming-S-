from django.db import models
from django.contrib.auth.models import User


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
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    
    def __str__(self):
        return self.name
    

class AnimalPhoto(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='photos', verbose_name="Животное")
    photo_url = models.URLField(max_length=500, verbose_name="URL Фото", default='https://example.com/default.jpg')

    def __str__(self):
        return f"Фото для {self.animal.name}"


# forum

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment by {self.author} on {self.topic}'
    

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['content']
