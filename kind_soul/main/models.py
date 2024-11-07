from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image_url = models.URLField(
        max_length=500, blank=True)

    def __str__(self):
        return self.title
