from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from models import Article, Category


class ArticleResource(ModelResource):
    headline = fields.CharField(attribute='original_headline')
    category = fields.ToOneField('fuselage.api.CategoryResource', 'category')

    class Meta:
        authentication = Authentication()
        authorization = Authorization()
        resource_name = 'article'
        model = Article
        always_return_data = True
        queryset = Article.objects.all()
        excludes = [
            'original_headline',
            'new_headline',
            'article_uid',
            'created',
            'modified'
        ]

    def hydrate_category(self, bundle):
        short_name = bundle.data['category']['short_name']
        bundle.data['category'] = Category.objects.get(short_name=short_name)
        return bundle

    def dehydrate_category(self, bundle):
        return bundle.obj.category.short_name


class CategoryResource(ModelResource):
    class Meta:
        authentication = Authentication()
        authorization = Authorization()
        resource_name = 'category'
        model = Category
        always_return_data = True
        queryset = Category.objects.all()
