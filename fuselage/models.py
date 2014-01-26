from django.db import models

from uuidfield import UUIDField


CATEGORIES = (
    ('cockpit', 'Cockpit'),
    ('first', 'First Class'),
    ('business', 'Business Class'),
    ('coach', 'Coach'),
)


class Article(models.Model):
    article_uid = UUIDField(auto=True)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)
    headline = models.CharField(max_length=1000)
    modified = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=2000, unique=True)

    class Meta:
        db_table = 'articles'
