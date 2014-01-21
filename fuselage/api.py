from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource

from models import Article


class ArticleResource(ModelResource):
    category = fields.CharField()
    created = fields.DateTimeField()
    headline = fields.CharField()
    modified = fields.DateTimeField()
    url = fields.CharField()

    class Meta:
        authentication = Authentication()
        resource_name = 'article'
        model = Article
        always_return_data = True
