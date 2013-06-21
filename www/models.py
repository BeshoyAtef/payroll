from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.utils.timezone import utc
import datetime
import calendar
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

    '''Tharwat --- This method is used to compute the yearly attendance for a specific employee in order to determine his yearly
    attendance and show the total in each month of the year. it takes in 2 variables, the employee and the desired year.
    it then returns an array of the result'''
    def employee_yearly_attendance_report(self, desired_year):
        employee = Employee.objects.get(id = self.id)
        all_attendances = Attendance.objects.filter(date__year = desired_year, employee_id = self.id)    
        #dictonary to gather monthly related results
        attendance_month_aggregate = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
        Dict_array = []

        #loop through all attendances in the year
        for attendance in all_attendances:
            working_hours = ((attendance.check_out - attendance.check_in).seconds)/60/60
            attendance_month_aggregate[attendance.date.month] += working_hours

        #loop around the dictonary to group them in order and place them in the array
        for key in attendance_month_aggregate:
            temp_dict = {key: (attendance_month_aggregate[key])}
            # total_number_of_working_hours += attendance_month_aggregate[key]
            Dict_array.append(temp_dict)
            temp_dict = {}

        # average = total_number_of_working_hours/number_of_employees
        return Dict_array

    '''Tharwat --- This method is used to compute the monthly attendance for a specific employee in order to determine his daily
    attendance and show the total in each day of the month. it takes in 3 variables, the employee, thr desired_month and the desired year.
    it then returns an array of the result'''
    def employee_monthly_attendance_report(self, desired_year, desired_month):
        employee = Employee.objects.get(id = self.id)
        all_attendances = Attendance.objects.filter(date__year = desired_year, date__month = desired_month, employee_id = self.id)    
        list_of_attendance_per_day = [0]*31
        total_hours = 0

        #loops on all attendances and checks which one belongs to which day and then inserts it in the corresponding index in 
        # the array
        for attendance in all_attendances:
            #day starts at 0 since first index = 0
            day = 0
            while day <= 31:
                if attendance.date.day == (day + 1):
                    #calculate hours worked during the day
                    hours = ((attendance.check_out - attendance.check_in).seconds)/60/60
                    #adds value to the list in the corresponding index
                    list_of_attendance_per_day[day] = list_of_attendance_per_day[day] + hours
                    day = day + 1
                else:
                    day = day + 1

        #loop on the list to calculate the total hours worked during the month
        for x in list_of_attendance_per_day:
            total_hours = total_hours + x

        # Dict = {'List of Attendance per Day' : list_of_attendance_per_day}
        Dict = list_of_attendance_per_day

        return Dict
    
    def __unicode__(self):
        return self.name

#Attendance: Date, Checkin time, Checkout time, Employee
class Attendance(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    employee = models.ForeignKey(Employee)


            

'''This method is used to get the attendance report for all employees during a specific year. the method takes in the 
    year of which the user wishes to view the result. it will then add the results related to each month together in a
    dictionary. after its done it will place them all in an array. it returns an array of dictionaries'''
def company_wide_yearly_attendance_report(desired_year):
    all_employees = Employee.objects.all()
    all_attendances = Attendance.objects.filter(date__year = desired_year)
    number_of_employees = len(all_employees)
    total_number_of_working_hours = 0
    #dictonary to gather monthly related results
    attendance_month_aggregate = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
    #array to group the dictonaries in the right order
    Dict_array = []
    months = 1

    #loop through the year
    while months <= 12:
        #calculates the monthly result
        monthly_result = company_wide_monthly_attendance_report(desired_year, months)
        for x in monthly_result:
            attendance_month_aggregate[months] += x
        months += 1

    #loop around the dictonary to group them in order and place them in the array
    for key in attendance_month_aggregate:
        temp_dict = {key: (attendance_month_aggregate[key])}
        # total_number_of_working_hours += attendance_month_aggregate[key]
        Dict_array.append(temp_dict)
        temp_dict = {}

    # average = total_number_of_working_hours/number_of_employees
    return Dict_array

'''Tharwat --- This method is used to get the attendance report for all employees during a certain month.
    it takes in a year and the month the user wishes to view. '''
def company_wide_monthly_attendance_report(desired_year, desired_month):
    all_attendances = Attendance.objects.filter(date__year = desired_year, date__month = desired_month)
    number_of_employees = len(Employee.objects.all())
    #create an empty list with the number of days (biggest = 31)
    list_of_attendance_per_day = [0]*31
    total_hours = 0

    #loops on all attendances and checks which one belongs to which day and then inserts it in the corresponding index in 
    # the array
    for attendance in all_attendances:
        #day starts at 0 since first index = 0
        day = 0
        while day <= 31:
            if attendance.date.day == (day + 1):
                #calculate hours worked during the day
                hours = ((attendance.check_out - attendance.check_in).seconds)/60/60
                #adds value to the list in the corresponding index
                list_of_attendance_per_day[day] = list_of_attendance_per_day[day] + hours
                day = day + 1
            else:
                day = day + 1

    #loop on the list to calculate the total hours worked during the month
    for x in list_of_attendance_per_day:
        total_hours = total_hours + x

    # Dict = {'List of Attendance per Day' : list_of_attendance_per_day}
    Dict = list_of_attendance_per_day

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
    #Dictonary to group month related results together
    batch_month_aggregate = {}
    #Array to order the dictonary 
    Dict_array = []

    for batch in total_batches:
        #month name stored by default in Django
        month = calendar.month_name[batch.date.month]
        #if month hasent been already added it is added as the key and the value is added. 
        #Else add the new value with the previous one
        if month not in batch_month_aggregate:
            batch_month_aggregate[month] = batch.size
        else: 
            batch_month_aggregate[month] += batch.size

    #loop around the dictonary to group them in order and place them in the array
    for key in batch_month_aggregate:
        temp_dict = {key: (batch_month_aggregate[key])}
        Dict_array.append(temp_dict)
        temp_dict = {}

    #sumes up all batch sizes
    total_batches_size = sum(batch_month_aggregate.values())
    batch_per_employee = total_batches_size/number_of_employees

    return Dict_array, total_batches_size, batch_per_employee

'''Tharwat --- This method returns the producivity output report for a specific month for all the employees. It takes in the
year and month from the user and then lists the productivity for each day of the month.'''

def company_wide_output_monthly_report(desired_year, desired_month):
    total_batches = Batch.objects.filter(date__year = desired_year, date__month = desired_month)
    number_of_employees = len(Employee.objects.all())
    #Array to order dictionary
    Dict_array = []
    #array of days (biggest = 31)
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
    def __unicode__(self):
		return self.employee.name

'''Tharwat--- This method returns the salary report for all employees for a specific year that is chosen by the user. It takes
the year form the user and then checks for the amount of salaries that are paid each month for the chosen year'''

def company_wide_salary_report(desired_year):
    yearly_payments = Payment.objects.filter(date__year = desired_year)
    #Dictonary to store results that are monthly related
    salary_month_aggregate = {}
    #Array to order the dictionary
    Dict_array = []


    for payment in yearly_payments:
        #month name stored by default in Django 
        month = calendar.month_name[payment.date.month]
        
        #if month hasent been already added it is added as the key and the value is added.
        # Else add the new value with the previous one    
        if month not in salary_month_aggregate: salary_month_aggregate[month] = payment.amount
        else: salary_month_aggregate[month] += payment.amount

    #loop around the dictonary to group them in order and place them in the array
    for key in salary_month_aggregate:
        temp_dict = {key: (salary_month_aggregate[key])}
        Dict_array.append(temp_dict)
        temp_dict = {}

    total_salaries = sum(salary_month_aggregate.values())
    return Dict_array
    
#Loans: ID, Date, Employee ID, Amount
class Loan(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    employee = models.ForeignKey(Employee)
    amount = models.IntegerField()

    def __unicode__(self):
    	return self.employee.name + str("__") + str(self.amount)
