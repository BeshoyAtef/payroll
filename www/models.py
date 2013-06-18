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

    def working_hours(self, date_start_year, date_start_month, date_start_day, date_end_year, date_end_month, date_end_day, type_query):
        date_start = datetime.datetime(date_start_year, date_start_month, date_start_day)
        date_end = datetime.datetime(date_end_year, date_end_month, date_end_day)
        attendances = {}
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
        return working_hours

#Attendance: Date, Checkin time, Checkout time, Employee
class Attendance(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    employee = models.ForeignKey(Employee)

def company_wide_yearly_attendance_report(desired_year):
    all_employees = Employee.objects.all()
    all_attendances = Attendance.objects.all()
    number_of_employees = len(all_employees)

    Jan = Feb = March = April = May = June = July = August = September = October = November = December = 0

    for attendance in all_attendances:
        print attendance.employee
        if attendance.date.month == 1:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed") 
            Jan = Jan + working_hours
        if attendance.date.month == 2:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            Feb = Feb + working_hours
        if attendance.date.month == 3:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            March = March + working_hours
        if attendance.date.month == 4:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            April = April + working_hours
        if attendance.date.month == 5:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            May = May + working_hours
        if attendance.date.month == 6:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            June = June + working_hours
        if attendance.date.month == 7:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            July = July + working_hours
        if attendance.date.month == 8:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            August = August + working_hours
        if attendance.date.month == 9:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            September = September + working_hours
        if attendance.date.month == 10:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            October = October + working_hours
        if attendance.date.month == 11:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            November = November + working_hours
        if attendance.date.month == 12:
            employee = attendance.employee
            working_hours = employee.working_hours(desired_year, 1, 1, desired_year + 1, 1, 1, "fixed")
            December = December + working_hours

    total_number_of_working_hours = Jan + Feb + March + April + May + June + July + August + September + October + November + December
    average = total_number_of_working_hours/number_of_employees

    Dict = {'Jan': Jan, 'Feb': Feb, 'March': March, 'April': April, 'May': May, 'June': June, 'July': July, 'August': August, 
    ' September': September, 'October': October, 'November': November, 'December': December, 'Total Number of Working Hours': total_number_of_working_hours, 
    'Average of working hours/Employee': average}

    return Dict

def company_wide_monthly_attendance_report(desired_year, desired_month):
    all_attendances = Attendance.objects.filter(date__year = desired_year, date__month = desired_month)
    number_of_employees = len(Employee.objects.all())
    list_of_attendance_per_day = [0]*31
    
    total_hours = 0

    for attendance in all_attendances:
        day = 0
        while day <= 31:
            if attendance.date.day == (day + 1):
                hours = (attendance.check_out - attendance.check_in).seconds/60/60
                list_of_attendance_per_day[day] = list_of_attendance_per_day[day] + hours
                day = day + 1
            else:
                day = day + 1

    for x in list_of_attendance_per_day:
        total_hours = total_hours + x

    print total_hours
    print list_of_attendance_per_day
    Dict = {'List of Attendance per Day' : list_of_attendance_per_day, 'Total Hours of Work': total_hours}

    return Dict

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

'''Tharwat --- This method returns the productivity report for a whole year that is chosen by the user. It takes the desired year
from the user and then generates the list.'''

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

'''Tharwat --- This method returns the producivity output report for a specific month for all the employees. It takes in the
year and month from the user and then lists the productivity for each day of the month.'''

def company_wide_output_monthly_report(desired_year, desired_month):
    total_batches = Batch.objects.filter(date__year = desired_year, date__month = desired_month)
    number_of_employees = len(Employee.objects.all())
    list_of_output_per_day = [0]*31
    count = 0
    total = 0 
    for batch in total_batches:
        day = batch.date.day - 1 
        list_of_output_per_day[day] = list_of_output_per_day[day] + batch.size 

    for x in list_of_output_per_day:
        total = total + x

    batch_per_employee = total/number_of_employees
    Dict = {'list_of_output_per_day': list_of_output_per_day, 'Total Produced': total, 'batch_per_employee': batch_per_employee}

    return Dict


#Payment: ID, Date, Employee ID, amount
class Payment(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    employee = models.ForeignKey(Employee)
    amount = models.IntegerField()


'''Tharwat--- This method returns the salary report for all employees for a specific year that is chosen by the user. It takes
the year form the user and then checks for the amount of salaries that are paid each month for the chosen year'''

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
