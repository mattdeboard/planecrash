from django.db import models

from uuidfield import UUIDField


class ArticleManager(models.Manager):
    def by_category(self, short_name):
        """Retrieve all the articles for a given category short name.

        This differs from the standard
        `filter(category__short_name='foo')` because it also limits the
        number of results to the value of the `seats` property of the
        category. If you don't need this limitation applied, just use
        `filter(category__short_name='foo')`.

        """
        category = Category.objects.get(short_name=short_name)
        qs = super(ArticleManager, self).get_queryset()\
                                        .select_related('category')\
                                        .filter(category=category)\
                                        .order_by('priority')
        return qs[:category.seats]


class Article(models.Model):
    article_uid = UUIDField(auto=True)
    category = models.ForeignKey('Category', null=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    new_headline = models.CharField(max_length=1000, null=True)
    original_headline = models.CharField(max_length=1000)
    priority = models.IntegerField(null=True)
    url = models.URLField(max_length=2000, unique=True)

    objects = ArticleManager()

    class Meta:
        db_table = 'articles'

    def __repr__(self):
        return "<Article: uuid:%s>" % self.article_uid

    def __unicode__(self):
        return self.new_headline or self.original_headline


class Category(models.Model):
    seats = models.IntegerField()
    title = models.CharField(max_length=20, db_index=True, unique=True)
    short_name = models.CharField(max_length=20, db_index=True, unique=True)
    priority = models.IntegerField()

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    def __repr__(self):
        return "<Category: %s>" % self.title

    def __unicode__(self):
        return self.title
