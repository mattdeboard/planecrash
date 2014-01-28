from django.conf import settings
from django.conf.urls import patterns, include, static, url
from django.contrib import admin

from tastypie.api import Api
from fuselage.api import ArticleResource, CategoryResource

admin.autodiscover()
api = Api(api_name='v1')
api.register(ArticleResource())
api.register(CategoryResource())
urlpatterns = patterns(
    '',
    (r'^', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'fuselage.views.index'),
)


urlpatterns += static.static('/static/admin/',
                             document_root=settings.STATIC_ROOT)
