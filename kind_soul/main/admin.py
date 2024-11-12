from django.contrib import admin
from .models import News, Animal

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Поля, которые существуют в модели News
    search_fields = ('title',)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')  # Поля, которые существуют в модели Animal
    list_filter = ('gender',)
    search_fields = ('name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Animal, AnimalAdmin)