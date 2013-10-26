# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Specialty'
        db.create_table(u'users_specialty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=63)),
        ))
        db.send_create_signal(u'users', ['Specialty'])

        # Adding model 'Student'
        db.create_table(u'users_student', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.User'], unique=True, primary_key=True)),
            ('specialty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Specialty'])),
        ))
        db.send_create_signal(u'users', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Specialty'
        db.delete_table(u'users_specialty')

        # Deleting model 'Student'
        db.delete_table(u'users_student')


    models = {
        u'users.specialty': {
            'Meta': {'object_name': 'Specialty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'})
        },
        u'users.student': {
            'Meta': {'object_name': 'Student', '_ormbases': [u'users.User']},
            'specialty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Specialty']"}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'card_key': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '63'})
        }
    }

    complete_apps = ['users']