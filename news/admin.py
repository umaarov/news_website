from django.contrib import admin
from .models import Category, NewsArticle

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'body')

admin.site.register(Category, CategoryAdmin)
admin.site.register(NewsArticle, NewsArticleAdmin)
