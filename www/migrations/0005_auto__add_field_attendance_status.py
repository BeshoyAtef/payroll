# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Attendance.status'
        db.add_column(u'www_attendance', 'status',
                      self.gf('django.db.models.fields.CharField')(default='M', max_length=3),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Attendance.status'
        db.delete_column(u'www_attendance', 'status')


    models = {
        u'www.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'check_in': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'null': 'True'}),
            'check_out': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 3, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_exeption': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reason': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '3'})
        },
        u'www.attendanceexception': {
            'Meta': {'object_name': 'AttendanceException'},
            'attendance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Attendance']"}),
            'check_in': ('django.db.models.fields.DateTimeField', [], {}),
            'check_out': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'www.batch': {
            'Meta': {'object_name': 'Batch'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 3, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Item']"}),
            'item_price': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '100'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'www.companydowntime': {
            'Meta': {'object_name': 'CompanyDowntime'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 3, 0, 0)'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'www.csvfile': {
            'Meta': {'object_name': 'CsvFile'},
            'attendence_sheet': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'www.employee': {
            'Meta': {'object_name': 'Employee'},
            'acc_no': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'salary': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ssn': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'www.item': {
            'Meta': {'object_name': 'Item'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'www.loan': {
            'Meta': {'object_name': 'Loan'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 3, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'www.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 3, 3, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['www']