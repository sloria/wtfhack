# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Repo.description'
        db.alter_column('base_repo', 'description', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'Repo.full_name'
        db.alter_column('base_repo', 'full_name', self.gf('django.db.models.fields.CharField')(max_length=500))

    def backwards(self, orm):

        # Changing field 'Repo.description'
        db.alter_column('base_repo', 'description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))

        # Changing field 'Repo.full_name'
        db.alter_column('base_repo', 'full_name', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        'base.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learn_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'base.repo': {
            'Meta': {'object_name': 'Repo'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'repos'", 'to': "orm['base.Language']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['base']