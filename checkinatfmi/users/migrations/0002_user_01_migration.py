# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.name'
        db.delete_column(u'users_user', 'name')

        # Adding field 'User.first_name'
        db.add_column(u'users_user', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)

        # Adding field 'User.last_name'
        db.add_column(u'users_user', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'User.name'
        db.add_column(u'users_user', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63),
                      keep_default=False)

        # Deleting field 'User.first_name'
        db.delete_column(u'users_user', 'first_name')

        # Deleting field 'User.last_name'
        db.delete_column(u'users_user', 'last_name')


    models = {
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'card_key': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'})
        }
    }

    complete_apps = ['users']