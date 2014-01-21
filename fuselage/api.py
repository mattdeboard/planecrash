from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from models import Article


class ArticleResource(ModelResource):

    class Meta:
        authentication = Authentication()
        authorization = Authorization()
        resource_name = 'article'
        model = Article
        always_return_data = True
        queryset = Article.objects.all()
