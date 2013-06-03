# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Client.status'
        db.alter_column(u'clients_client', 'status', self.gf('django.db.models.fields.BooleanField')())

    def backwards(self, orm):

        # Changing field 'Client.status'
        db.alter_column(u'clients_client', 'status', self.gf('django.db.models.fields.NullBooleanField')(null=True))

    models = {
        u'clients.client': {
            'Meta': {'object_name': 'Client'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['clients']