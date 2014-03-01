# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyCsvFile'
        db.create_table(u'www_mycsvfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Ac_No', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('finger_Print', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('machine', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'www', ['MyCsvFile'])


    def backwards(self, orm):
        # Deleting model 'MyCsvFile'
        db.delete_table(u'www_mycsvfile')


    models = {
        u'www.attendance': {
            'Meta': {'model_name': 'Attendance'},
            'check_in': ('django.db.models.fields.DateTimeField', [], {}),
            'check_out': ('django.db.models.fields.DateTimeField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 17, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'www.attendanceexception': {
            'Meta': {'model_name': 'AttendanceException'},
            'attendance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Attendance']"}),
            'check_in': ('django.db.models.fields.DateTimeField', [], {}),
            'check_out': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'www.batch': {
            'Meta': {'model_name': 'Batch'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 17, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Item']"}),
            'item_price': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'www.companydowntime': {
            'Meta': {'model_name': 'CompanyDowntime'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 17, 0, 0)'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'www.employee': {
            'Meta': {'model_name': 'Employee'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'salary': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ssn': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'www.item': {
            'Meta': {'model_name': 'Item'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'www.loan': {
            'Meta': {'model_name': 'Loan'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 17, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'www.mycsvfile': {
            'Ac_No': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'ordering': "['Ac_No']", 'model_name': 'MyCsvFile'},
            'finger_Print': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'www.payment': {
            'Meta': {'model_name': 'Payment'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 17, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['www']