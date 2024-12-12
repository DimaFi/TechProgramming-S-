from django.contrib import admin
from .models import News, Animal, AnimalPhoto, Topic, Comment

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Поля, которые существуют в модели News
    search_fields = ('title',)


class AnimalPhotoInline(admin.TabularInline):
    model = AnimalPhoto
    extra = 1

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')  # Поля, которые существуют в модели Animal
    list_filter = ('gender',)
    search_fields = ('name',)
    inlines = [AnimalPhotoInline] # управление фотографиями
    options = ('option')



admin.site.register(News, NewsAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalPhoto)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'description']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'topic', 'created_at']
    search_fields = ['content']