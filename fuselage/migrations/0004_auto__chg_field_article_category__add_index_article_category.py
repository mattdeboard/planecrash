# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Article.category' to match new field type.
        db.rename_column('articles', 'category', 'category_id')
        # Changing field 'Article.category'
        db.alter_column('articles', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuselage.Category'], null=True))
        # Adding index on 'Article', fields ['category']
        db.create_index('articles', ['category_id'])


    def backwards(self, orm):
        # Removing index on 'Article', fields ['category']
        db.delete_index('articles', ['category_id'])


        # Renaming column for 'Article.category' to match new field type.
        db.rename_column('articles', 'category_id', 'category')
        # Changing field 'Article.category'
        db.alter_column('articles', 'category', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

    models = {
        u'fuselage.article': {
            'Meta': {'object_name': 'Article', 'db_table': "'articles'"},
            'article_uid': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fuselage.Category']", 'null': 'True'}),
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