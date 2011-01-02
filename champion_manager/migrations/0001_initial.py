# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'City'
        db.create_table('champion_manager_city', (
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('champion_manager', ['City'])

        # Adding model 'Champion'
        db.create_table('champion_manager_champion', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=18)),
        ))
        db.send_create_signal('champion_manager', ['Champion'])

        # Adding M2M table for field cities on 'Champion'
        db.create_table('champion_manager_champion_cities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('champion', models.ForeignKey(orm['champion_manager.champion'], null=False)),
            ('city', models.ForeignKey(orm['champion_manager.city'], null=False))
        ))
        db.create_unique('champion_manager_champion_cities', ['champion_id', 'city_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'City'
        db.delete_table('champion_manager_city')

        # Deleting model 'Champion'
        db.delete_table('champion_manager_champion')

        # Removing M2M table for field cities on 'Champion'
        db.delete_table('champion_manager_champion_cities')
    
    
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['champion_manager']
