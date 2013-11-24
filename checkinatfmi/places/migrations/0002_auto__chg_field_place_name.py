# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Place.name'
        db.alter_column(u'places_place', 'name', self.gf('django.db.models.fields.CharField')(max_length=63, null=True))

    def backwards(self, orm):

        # Changing field 'Place.name'
        db.alter_column(u'places_place', 'name', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

    models = {
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True'})
        }
    }

    complete_apps = ['places']