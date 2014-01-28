from django.contrib import admin

from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('category', 'priority', 'original_headline', 'created')
    search_fields = ('original_headline', 'url', 'category__title')
    list_filter = ('category__title',)

admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'short_name', 'seats')

admin.site.register(Category, CategoryAdmin)
