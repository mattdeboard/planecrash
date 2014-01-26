# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table('articles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article_uid', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=2000)),
        ))
        db.send_create_signal(u'fuselage', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table('articles')


    models = {
        u'fuselage.article': {
            'Meta': {'object_name': 'Article', 'db_table': "'articles'"},
            'article_uid': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '2000'})
        }
    }

    complete_apps = ['fuselage']