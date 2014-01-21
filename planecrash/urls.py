from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
from fuselage.api import ArticleResource

admin.autodiscover()
api = Api(api_name='v1')
api.register(ArticleResource())
urlpatterns = patterns(
    '',
    (r'^', include(api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
