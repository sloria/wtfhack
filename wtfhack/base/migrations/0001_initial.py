# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Repo'
        db.create_table('base_repo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('base', ['Repo'])


    def backwards(self, orm):
        # Deleting model 'Repo'
        db.delete_table('base_repo')


    models = {
        'base.repo': {
            'Meta': {'object_name': 'Repo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['base']