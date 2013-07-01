from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.utils.timezone import utc
import datetime
from datetime import timedelta

from django.db.models import Sum , Avg 



from itertools import chain
from django.utils.translation import ugettext_lazy as _


class Employee(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=100)     
    email = models.EmailField(verbose_name=_('Email'), max_length=254, unique=True)
    mobile = models.IntegerField(verbose_name=_('Mobile'), default=0)
    ssn = models.IntegerField(verbose_name=_('SSN'), default=0)        
    salary = models.IntegerField(verbose_name=_('Salary'), default=0)
    acc_no = models.IntegerField(verbose_name=_('AccNum'), default=0)
    
    REQUIRED_FIELDS = ['name']

    class Meta:
       verbose_name = _('Employee')
       verbose_name_plural = _('Employees')

    def __unicode__(self):
        return self.name+"-"+str(self.mobile)

    #Mohamed Awad
    #this def returns the working hours of any employee
    #given to it a range of integers that represent start and end years, months and days
    def working_hours(self, date_start_year, date_start_month, date_start_day, date_end_year, date_end_month, date_end_day, type_query):
        date_start = datetime.datetime(date_start_year, date_start_month, date_start_day)
        date_end = datetime.datetime(date_end_year, date_end_month, date_end_day)
        attendances = {}
        #this if condition is to check whether the date is fixed or custom
        #a fixed range means a specific month or year
        #a custom range means any range of days
        if type_query == "fixed":
            attendances = Attendance.objects.filter(date__range = [date_start, date_end], employee = self).exclude(date = date_end)
        else:
            attendances = Attendance.objects.filter(date__range = [date_start, date_end], employee = self)
        working_seconds = 0
        working_minutes = 0
        working_hours = 0
        for attendance in attendances:
            working_timedelta = attendance.check_out - attendance.check_in
            working_seconds = working_seconds + working_timedelta.seconds
        working_hours = working_seconds/60/60
        return working_hours

    #Mohamed Awad
    #this def returns the number of products of any employee
    #given to it a range of integers that represent start and end years, months and days.
    def productivity(self, date_start_year, date_start_month, date_start_day, date_end_year, date_end_month, date_end_day, type_query):
        date_start = datetime.datetime(date_start_year, date_start_month, date_start_day)
        date_end = datetime.datetime(date_end_year, date_end_month, date_end_day)
        total_products = {}
        #this if condition is to check whether the date is fixed or custom
        #a fixed range means a specific month or year
        #a custom range means any range of days
        if type_query == "fixed":
            total_products = Batch.objects.filter(date__range = [date_start, date_end], employee = self).exclude(date = date_end)
        else:
            total_products = Batch.objects.filter(date__range = [date_start, date_end], employee = self)
        items = 0
        for product in total_products:
            items = items + product.size
        return items
    
    #Mohamed Awad
    #this def returns the total payement of an employee
    #of a specific start date and end date
    def payement_yearly(self, date_start_year, date_start_month, date_start_day, date_end_year, date_end_month, date_end_day):
        salary = self.salary
        date_start = datetime.datetime(date_start_year, date_start_month, date_start_day)
        date_end = datetime.datetime(date_end_year, date_end_month, date_end_day)
        batches = Batch.objects.filter(employee = self, date__range = [date_start, date_end]).exclude(date = date_end)
        for batch in batches:
            amounts_to_pay = batch.item_price*batch.size
            salary = salary + amounts_to_pay
        return salary

    #Mohamed Awad
    #this def returns the total payement of an employee
    #of a specific start date and end date
    def payement_monthly(self, date_start_year, date_start_month, date_start_day, date_end_year, date_end_month, date_end_day):
        salary = 0
        date_start = datetime.datetime(date_start_year, date_start_month, date_start_day)
        date_end = datetime.datetime(date_end_year, date_end_month, date_end_day)
        batches = Batch.objects.filter(employee = self, date__range = [date_start, date_end])
        for batch in batches:
            amounts_to_pay = batch.item_price*batch.size
            salary = salary + amounts_to_pay
        return salary

    def get_attendance(self, date_start_year, date_start_month, date_start_day, date_end_year, date_end_month, date_end_day):
        date_start = datetime.datetime(date_start_year, date_start_month, date_start_day)
        date_end = datetime.datetime(date_end_year, date_end_month, date_end_day)
        attendance=Attendance.objects.filter(employee=self,date__range=[date_start,date_end])
        attendance_exptions=AttendanceException.objects.filter(attendance__in=[o.id for o in attendance], check_in__range = [date_start, date_end])
        attendance=Attendance.objects.filter(employee=self, date__range=[date_start,date_end]).exclude(id__in=[o.attendance.id for o in attendance_exptions])
        final_attendace=list(chain(attendance, attendance_exptions))
        return final_attendace

    REQUIRED_FIELDS = ['name']  



#Attendance: Date, Checkin time, Checkout time, Employee
class Attendance(models.Model):
    date = models.DateTimeField(verbose_name=_('Date'), default=datetime.datetime.now())
    check_in = models.DateTimeField(verbose_name=_('CheckIn'), null=True)
    check_out = models.DateTimeField(verbose_name=_('CheckOut'), null = True)
    employee = models.ForeignKey(Employee, verbose_name=_('Employee'))

    class Meta:
       verbose_name = _('Attendance')
       verbose_name_plural = _('Attendances')

    def __unicode__(self):
        s=self.employee.name+"-"+str(self.date.date())
        return s

def get_attendance(employee):
    attendance=Attendance.objects.filter(employee=employee)
    attendance_exptions=AttendanceException.objects.filter(attendance__in=[o.id for o in attendance])
    attendance=Attendance.objects.filter(employee=employee).exclude(id__in=[o.attendance.id for o in attendance_exptions])
    final_attendace=list(chain(attendance, attendance_exptions))
    return final_attendace
    

#Attendance Exception: Attendance ID, Checkin time, Checkout time
class AttendanceException(models.Model):
    attendance = models.ForeignKey(Attendance, verbose_name=_('Attendance'))
    check_in = models.DateTimeField(verbose_name =_('CheckIn'))
    check_out = models.DateTimeField(verbose_name =_('CheckOut'))

    class Meta:
       verbose_name = _('AttendanceException')
       verbose_name_plural = _('AttendanceExceptions')


#Company Downtime: Date, start time, end time
class CompanyDowntime(models.Model):
    date = models.DateTimeField(verbose_name=_('Date'), default=datetime.datetime.now())
    start_time = models.DateTimeField(verbose_name=_('StartTime'))
    end_time = models.DateTimeField(verbose_name=_('EndTime'))

    class Meta:
       verbose_name = _('CompanyDowntime')
       verbose_name_plural = _('CompanyDowntimes')

#Item: ID, name ,value
''' "identifier" has been used for the naming of the id , as django by default have an id for each model 
and using and id again will be confusing  and a value has been added which represent the money the employee should get from this model'''
class Item(models.Model):
    identifier = models.CharField(verbose_name =_('Identifier'), max_length=100,unique=True)  
    description = models.CharField(verbose_name =_('description'), max_length=100)  
    value = models.IntegerField(verbose_name =_('Value'), default=0)

    REQUIRED_FIELDS = ['identifier']  

    class Meta:
       verbose_name = _('Item')
       verbose_name_plural = _('Items')

    def __unicode__(self):
        s=self.identifier+"-"+self.description+"-"+str(self.value)
        return s

#Batches: ID, Employee ID, Date, item ID, Piece price, Size
class Batch(models.Model):
<<<<<<< HEAD
    employee = models.ForeignKey(Employee, verbose_name=_('Employee'))
    date = models.DateTimeField(default=datetime.datetime.now(), verbose_name =_('Date'))
    item = models.ForeignKey(Item, verbose_name=_('Item'))
    item_price = models.IntegerField(verbose_name =_('ItemPrice'))
    size = models.IntegerField(default=0, verbose_name =_('Size'))
    reason = models.CharField(max_length=100,default="none", verbose_name =_('Reason1'))  

    class Meta:
       verbose_name = _('Batch')
       verbose_name_plural = _('Batches')

    def __unicode__(self):
        s=self.employee.name+"-"+str(self.item)+"-"+str(self.item_price)
        return s
#Payment: ID, Date, Employee ID, amount
class Payment(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now(), verbose_name =_('Date'))
    employee = models.ForeignKey(Employee, verbose_name =_('Employee'))
    amount = models.IntegerField(verbose_name =_('Amount'))

    class Meta:
       verbose_name = _('Payment')
       verbose_name_plural = _('Payments')

    def __unicode__(self):
        s=self.employee.name+"-"+self.amount+"-"+self.date
        return s
#Loans: ID, Date, Employee ID, Amount
class Loan(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now(), verbose_name=_('Date'))
    employee = models.ForeignKey(Employee, verbose_name=_('Employee'))
    amount = models.IntegerField(verbose_name =_('Amount'))

    class Meta:
       verbose_name = _('Loan')
       verbose_name_plural = _('Loans')

    def __unicode__(self):
        return self.employee.name + str("__") + str(self.amount)

class CsvFile(models.Model):
    attendence_sheet = models.FileField(upload_to='media')

    def __unicode__(self):
        return self.employee.name + str("__") + str(self.amount)
