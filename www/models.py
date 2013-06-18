from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.utils.timezone import utc
import datetime
from datetime import timedelta

class Employee(models.Model):
    name = models.CharField(max_length=100)     
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.IntegerField(default=0)
    ssn = models.IntegerField(default=0)        
    salary = models.IntegerField(default=0)
    
    REQUIRED_FIELDS = ['name']  

    #Mohamed Awad
    #this def returns the working hours of any employee
    #given to it a range of integers that represent start and end years, months and days.
    def working_hours(self, date_start_year, date_start_month, date_start_day, date_end_year, date_end_month, date_end_day):
        date_start = datetime.datetime(date_start_year, date_start_month, date_start_day)
        date_end = datetime.datetime(date_end_year, date_end_month, date_end_day)
        attendances = Attendance.objects.filter(date__range = [date_start, date_end], employee = self)
        working_seconds = 0
        working_minutes = 0
        working_hours = 0
        for attendance in attendances:
            working_timedelta = attendance.check_out - attendance.check_in
            working_seconds = working_seconds + working_timedelta.seconds
        working_hours = working_seconds/60/60
        working_seconds = working_seconds - working_hours*60*60
        working_minutes = working_seconds/60/60
        working_hours = working_hours + working_minutes
        working_seconds = (working_seconds - working_minutes*60)/60/60
        working_hours = working_hours + working_seconds
        return working_hours

    #Mohamed Awad
    #this def returns the number of products of any employee
    #given to it a range of integers that represent start and end years, months and days.
    def productivity(self, date_start_year, date_start_month, date_start_day, date_end_year, date_end_month, date_end_day):
        date_start = datetime.datetime(date_start_year, date_start_month, date_start_day)
        date_end = datetime.datetime(date_end_year, date_end_month, date_end_day)
        return len(Batch.objects.filter(date__range = [date_start, date_end], employee = self))


#Attendance: Date, Checkin time, Checkout time, Employee
class Attendance(models.Model):
    date = models.DateField(default=datetime.date.today)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    employee = models.ForeignKey(Employee)

    class Meta:
        ordering = ['date', 'employee']
        unique_together = ("date", "employee")
            

#Attendance Exception: Attendance ID, Checkin time, Checkout time
class AttendanceException(models.Model):
    attendance = models.ForeignKey(Attendance)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

#Company Downtime: Date, start time, end time
class CompanyDowntime(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

#Item: ID, name ,value
''' "identifier" has been used for the naming of the id , as django by default have an id for each model 
and using and id again will be confusing  and a value has been added which represent the money the employee should get from this model'''
class Item(models.Model):
    identifier = models.CharField(max_length=100,unique=True)  
    description = models.CharField(max_length=100)  
    value = models.IntegerField(default=0)

    REQUIRED_FIELDS = ['identifier']  

#Batches: ID, Employee ID, Date, item ID, Piece price, Size
class Batch(models.Model):
	employee = models.ForeignKey(Employee)
	date = models.DateTimeField(default=datetime.datetime.now())
	item = models.ForeignKey(Item)
	item_price = models.IntegerField()
	size = models.IntegerField(default=0)

#Payment: ID, Date, Employee ID, amount
class Payment(models.Model):
	date = models.DateTimeField(default=datetime.datetime.now())
	employee = models.ForeignKey(Employee)
	amount = models.IntegerField()

#Loans: ID, Date, Employee ID, Amount
class Loan(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    employee = models.ForeignKey(Employee)
    amount = models.IntegerField()

##