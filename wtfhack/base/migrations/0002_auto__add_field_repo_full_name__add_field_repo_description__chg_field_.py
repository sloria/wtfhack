# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Repo.full_name'
        db.add_column('base_repo', 'full_name',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'Repo.description'
        db.add_column('base_repo', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=300, null=True),
                      keep_default=False)


        # Changing field 'Repo.url'
        db.alter_column('base_repo', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Repo.language'
        db.alter_column('base_repo', 'language', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

    def backwards(self, orm):
        # Deleting field 'Repo.full_name'
        db.delete_column('base_repo', 'full_name')

        # Deleting field 'Repo.description'
        db.delete_column('base_repo', 'description')


        # Changing field 'Repo.url'
        db.alter_column('base_repo', 'url', self.gf('django.db.models.fields.URLField')(default=-1, max_length=200))

        # Changing field 'Repo.language'
        db.alter_column('base_repo', 'language', self.gf('django.db.models.fields.CharField')(default=1, max_length=40))

    models = {
        'base.repo': {
            'Meta': {'object_name': 'Repo'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['base']