# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.headline'
        db.delete_column('articles', 'headline')

        # Adding field 'Article.original_headline'
        db.add_column('articles', 'original_headline',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)

        # Adding field 'Article.new_headline'
        db.add_column('articles', 'new_headline',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Article.headline'
        db.add_column('articles', 'headline',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000),
                      keep_default=False)

        # Deleting field 'Article.original_headline'
        db.delete_column('articles', 'original_headline')

        # Deleting field 'Article.new_headline'
        db.delete_column('articles', 'new_headline')


    models = {
        u'fuselage.article': {
            'Meta': {'object_name': 'Article', 'db_table': "'articles'"},
            'article_uid': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'new_headline': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'original_headline': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '2000'})
        },
        u'fuselage.category': {
            'Meta': {'object_name': 'Category', 'db_table': "'categories'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'seats': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'})
        }
    }

    complete_apps = ['fuselage']