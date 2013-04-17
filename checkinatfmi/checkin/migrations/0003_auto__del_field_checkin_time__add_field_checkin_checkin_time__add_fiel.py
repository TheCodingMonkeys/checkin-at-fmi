# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Checkin.time'
        db.delete_column(u'checkin_checkin', 'time')

        # Adding field 'Checkin.checkin_time'
        db.add_column(u'checkin_checkin', 'checkin_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 17, 0, 0)),
                      keep_default=False)

        # Adding field 'Checkin.checkout_time'
        db.add_column(u'checkin_checkin', 'checkout_time',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Checkin.time'
        db.add_column(u'checkin_checkin', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 17, 0, 0)),
                      keep_default=False)

        # Deleting field 'Checkin.checkin_time'
        db.delete_column(u'checkin_checkin', 'checkin_time')

        # Deleting field 'Checkin.checkout_time'
        db.delete_column(u'checkin_checkin', 'checkout_time')


    models = {
        u'checkin.checkin': {
            'Meta': {'object_name': 'Checkin'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'checkin_time': ('django.db.models.fields.DateTimeField', [], {}),
            'checkout_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'card_key': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        }
    }

    complete_apps = ['checkin']