# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Activity'
        db.create_table(u'activities_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clients.Client'])),
            ('carrier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activities.Carrier'])),
        ))
        db.send_create_signal(u'activities', ['Activity'])

        # Adding model 'Carrier'
        db.create_table(u'activities_carrier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='U', max_length=2)),
            ('data', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
        ))
        db.send_create_signal(u'activities', ['Carrier'])

        # Adding model 'Borrow'
        db.create_table(u'activities_borrow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('borrower', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['identifications.Cardowner'])),
            ('borrow', self.gf('django.db.models.fields.related.ForeignKey')(related_name='borrowes', to=orm['activities.Activity'])),
            ('handback', self.gf('django.db.models.fields.related.ForeignKey')(related_name='handbackes', to=orm['activities.Activity'])),
        ))
        db.send_create_signal(u'activities', ['Borrow'])

        # Adding model 'Checkin'
        db.create_table(u'activities_checkin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checkin_activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='checkins', to=orm['activities.Activity'])),
            ('checkout_activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='checkouts', null=True, to=orm['activities.Activity'])),
        ))
        db.send_create_signal(u'activities', ['Checkin'])


    def backwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table(u'activities_activity')

        # Deleting model 'Carrier'
        db.delete_table(u'activities_carrier')

        # Deleting model 'Borrow'
        db.delete_table(u'activities_borrow')

        # Deleting model 'Checkin'
        db.delete_table(u'activities_checkin')


    models = {
        u'activities.activity': {
            'Meta': {'object_name': 'Activity'},
            'carrier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.Carrier']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clients.Client']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'activities.borrow': {
            'Meta': {'object_name': 'Borrow'},
            'borrow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'borrowes'", 'to': u"orm['activities.Activity']"}),
            'borrower': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['identifications.Cardowner']"}),
            'handback': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'handbackes'", 'to': u"orm['activities.Activity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'activities.carrier': {
            'Meta': {'object_name': 'Carrier'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            'data': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'})
        },
        u'activities.checkin': {
            'Meta': {'object_name': 'Checkin'},
            'checkin_activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'checkins'", 'to': u"orm['activities.Activity']"}),
            'checkout_activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'checkouts'", 'null': 'True', 'to': u"orm['activities.Activity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'clients.client': {
            'Meta': {'object_name': 'Client'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['university.Place']", 'null': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'identifications.cardowner': {
            'Meta': {'object_name': 'Cardowner'},
            'faculty_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'specialty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['university.Specialty']"}),
            'sudi_password': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'susi_name': ('django.db.models.fields.CharField', [], {'max_length': '63', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'blank': 'True'})
        },
        u'university.place': {
            'Meta': {'object_name': 'Place'},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'university.specialty': {
            'Meta': {'object_name': 'Specialty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['activities']