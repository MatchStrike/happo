# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'City.hashtag'
        db.add_column('champion_manager_city', 'hashtag', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True))
    
    
    def backwards(self, orm):
        
        # Deleting field 'City.hashtag'
        db.delete_column('champion_manager_city', 'hashtag')
    
    
    models = {
        'champion_manager.champion': {
            'Meta': {'object_name': 'Champion'},
            'cities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'champions'", 'to': "orm['champion_manager.City']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '18'})
        },
        'champion_manager.city': {
            'Meta': {'object_name': 'City'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hashtag': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['champion_manager']
