from django.contrib import admin

from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('original_headline', 'category', 'priority', 'new_headline',
                    'created')
    search_fields = ('original_headline', 'url', 'category__title')
    list_filter = ('category__title',)
    list_editable = ('new_headline', 'priority')
    ordering = ('category__priority', 'priority')

admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'short_name', 'seats')
    ordering = ('priority',)

admin.site.register(Category, CategoryAdmin)
