# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'clients_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('status', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('status_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'], null=True)),
        ))
        db.send_create_signal(u'clients', ['Client'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'clients_client')


    models = {
        u'clients.client': {
            'Meta': {'object_name': 'Client'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']", 'null': 'True'}),
            'status': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'status_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        }
    }

    complete_apps = ['clients']