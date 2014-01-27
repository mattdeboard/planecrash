from django.contrib import admin

from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('original_headline', 'category', 'created')
    search_fields = ('original_headline', 'url', 'category__title')
    list_filter = ('category__title',)

admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_name', 'seats', 'priority')

admin.site.register(Category, CategoryAdmin)
