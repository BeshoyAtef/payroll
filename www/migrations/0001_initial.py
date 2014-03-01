# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employee'
        db.create_table(u'www_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('mobile', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ssn', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('salary', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'www', ['Employee'])

        # Adding model 'Attendance'
        db.create_table(u'www_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 6, 11, 0, 0))),
            ('check_in', self.gf('django.db.models.fields.DateTimeField')()),
            ('check_out', self.gf('django.db.models.fields.DateTimeField')()),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['www.Employee'])),
        ))
        db.send_create_signal(u'www', ['Attendance'])

        # Adding model 'AttendanceException'
        db.create_table(u'www_attendanceexception', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attendance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['www.Attendance'])),
            ('check_in', self.gf('django.db.models.fields.DateTimeField')()),
            ('check_out', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'www', ['AttendanceException'])

        # Adding model 'CompanyDowntime'
        db.create_table(u'www_companydowntime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 6, 11, 0, 0))),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'www', ['CompanyDowntime'])

        # Adding model 'Item'
        db.create_table(u'www_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'www', ['Item'])

        # Adding model 'Batch'
        db.create_table(u'www_batch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['www.Employee'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 6, 11, 0, 0))),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['www.Item'])),
            ('item_price', self.gf('django.db.models.fields.IntegerField')()),
            ('size', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'www', ['Batch'])

        # Adding model 'Payment'
        db.create_table(u'www_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 6, 11, 0, 0))),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['www.Employee'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'www', ['Payment'])

        # Adding model 'Loan'
        db.create_table(u'www_loan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 6, 11, 0, 0))),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['www.Employee'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'www', ['Loan'])


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'www_employee')

        # Deleting model 'Attendance'
        db.delete_table(u'www_attendance')

        # Deleting model 'AttendanceException'
        db.delete_table(u'www_attendanceexception')

        # Deleting model 'CompanyDowntime'
        db.delete_table(u'www_companydowntime')

        # Deleting model 'Item'
        db.delete_table(u'www_item')

        # Deleting model 'Batch'
        db.delete_table(u'www_batch')

        # Deleting model 'Payment'
        db.delete_table(u'www_payment')

        # Deleting model 'Loan'
        db.delete_table(u'www_loan')


    models = {
        u'www.attendance': {
            'Meta': {'model_name': 'Attendance'},
            'check_in': ('django.db.models.fields.DateTimeField', [], {}),
            'check_out': ('django.db.models.fields.DateTimeField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 11, 0, 0)'}),
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
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 11, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Item']"}),
            'item_price': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'www.companydowntime': {
            'Meta': {'model_name': 'CompanyDowntime'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 11, 0, 0)'}),
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
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 11, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'www.payment': {
            'Meta': {'model_name': 'Payment'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 11, 0, 0)'}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['www.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['www']