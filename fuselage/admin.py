from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'category', 'created')
    search_fields = ('headline', 'url', 'category')
    list_filter = ('category',)

admin.site.register(Article, ArticleAdmin)
