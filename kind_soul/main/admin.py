from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Поля для отображения в админке
    search_fields = ('title',)  # Поле поиска
