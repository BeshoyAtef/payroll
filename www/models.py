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


#Attendance: Date, Checkin time, Checkout time, Employee
class Attendance(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    employee = models.ForeignKey(Employee)

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

def company_wide_output_yearly_report(desired_year):
    total_batches = Batch.objects.filter(date__year = desired_year)
    number_of_employees = len(Employee.objects.all())

    Jan = Feb = March = April = May = June = July = August = September = October = November = December = 0

    for batch in total_batches:
        if batch.date.month == 1:
            Jan = Jan + batch.size
        if batch.date.month == 2:
            Feb = Feb + batch.size
        if batch.date.month == 3:
            March = March + batch.size
        if batch.date.month == 4:
            April = April + batch.size
        if batch.date.month == 5:
            May = May + batch.size
        if batch.date.month == 6:
            June = June + batch.size
        if batch.date.month == 7:
            July = July + batch.size
        if batch.date.month == 8:
            August = August + batch.size
        if batch.date.month == 9:
            September = September + batch.size
        if batch.date.month == 10:
            October = October + batch.size
        if batch.date.month == 11:
            November = November + batch.size
        if batch.date.month == 12:
            December = December + batch.size

    total_batches_size = Jan + Feb + March + April + May + June + July + August + September + October + November + December
    batch_per_employee = total_batches_size/number_of_employees

    Dict = {'Jan': Jan, 'Feb': Feb, 'March': March, 'April': April, 'May': May, 'June': June, 'July': July, 'August': August, 
    ' September': September, 'October': October, 'November': November, 'December': December, 'batch_per_employee': batch_per_employee}

    return Dict

def company_wide_output_monthly_report(desired_year, desired_month):
    total_batches = Batch.objects.filter(date__year = desired_year, date__month = desired_month)
    number_of_employees = len(Employee.objects.all())
    list_of_output_per_day = []
    for batches in total_batches:
        day = batches.date.day
        print day
        print list_of_output_per_day[day]
        list_of_output_per_day[day] = list_of_output_per_day[day] + batches.size 


    number_of_items_in_list = len(list_of_output_per_day)
    list_of_output_per_day = range(number_of_items_in_list)
    total = sum(list_of_output_per_day) 
    batch_per_employee = total/number_of_employees

    Dict = {'list_of_output_per_day': list_of_output_per_day, 'batch_per_employee': batch_per_employee}

    return Dict


#Payment: ID, Date, Employee ID, amount
class Payment(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    employee = models.ForeignKey(Employee)
    amount = models.IntegerField()

def company_wide_salary_report(desired_year):
    yearly_payments = Payment.objects.filter(date__year = desired_year)
    Jan = Feb = March = April = May = June = July = August = September = October = November = December = 0  

    for payment in yearly_payments:
        print 'x'
        if payment.date.month == 1:
            Jan = Jan + payment.amount
        if payment.date.month == 2:
            Feb = Feb + payment.amount
        if payment.date.month == 3:
            March = March + payment.amount
        if payment.date.month == 4:
            April = April + payment.amount
        if payment.date.month == 5:
            May = May + payment.amount
        if payment.date.month == 6:
            June = June + payment.amount
        if payment.date.month == 7:
            July = July + payment.amount
        if payment.date.month == 8:
            August = August + payment.amount
        if payment.date.month == 9:
            September = September + payment.amount
        if payment.date.month == 10:
            October = October + payment.amount
        if payment.date.month == 11:
            November = November + payment.amount
        if payment.date.month == 12:
            December = December + payment.amount

    Dict = {'Jan': Jan, 'Feb': Feb, 'March': March, 'April': April, 'May': May, 'June': June, 'July': July, 'August': August, 
    ' September': September, 'October': October, 'November': November, 'December': December}
    
    return Dict

#Loans: ID, Date, Employee ID, Amount
class Loan(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    employee = models.ForeignKey(Employee)
    amount = models.IntegerField()

##