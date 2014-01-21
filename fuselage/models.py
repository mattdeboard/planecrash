from django.db import models

from uuidfield import UUIDField


CATEGORIES = (
    ('cockpit', 'Cockpit'),
    ('business', 'Business'),
    ('economy', 'Economy'),
)


class Article(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORIES)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)
    headline = models.CharField(max_length=1000)
    modified = models.DateTimeField(auto_now=True)
    article_uid = UUIDField(auto=True)
    url = models.URLField(max_length=2000)
