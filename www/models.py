from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.utils.timezone import utc
import datetime
# from datetime import timedelta
from itertools import chain
from constance import config


class Employee(models.Model):
    name = models.CharField(max_length=100)     
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.IntegerField(default=0)
    ssn = models.IntegerField(default=0)        
    salary = models.IntegerField(default=0)
    
    REQUIRED_FIELDS = ['name']  
    def __unicode__(self):
        return self.name+"-"+str(self.mobile)

#Attendance: Date, Checkin time, Checkout time, Employee
class Attendance(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    check_in = models.DateTimeField(null=True,default="")
    check_out = models.DateTimeField(null = True,default="")
    employee = models.ForeignKey(Employee)
    reason = models.CharField(max_length=100,default="",null=True)
    is_exeption = models.BooleanField(default=False)


    def __unicode__(self):
        s=self.employee.name+"-"+str(self.date.date())
        return s

# def get_attendance(employee):
#     attendance=Attendance.objects.filter(employee=employee)
#     .exclude(date.strftime("%A")=(CONFIG.Holidays).strftime("%A")) #execlude record in the holiday
#     .include()
#     return None

def cal_payment():
    employees=Employee.objects.all()
    for emp in employees:
        ckin=config.CHECKIN_TIME
        ckout=config.CHECKOut_TIME
        #get the Hours Worked (keep in mind the Company Start times & buffer-time & Company-Downtime)
        print ckin
        print ckout
        print ckout-ckin
        company_working_hours=ckout-ckin
        salary_per_hour=emp.salary/30/(ckin-ckout).hour()
        attendances=Attendance.objects.filter(employee=emp)
        hours_worked=0
        #attendance Loop to cal salary
        for att in attendances:
            if att.check_out.day()==att.check_in.day():
                hours_worked=hours_worked+(att.check_out.time()-att.check_in.time())
            else:
                return None#should rais an error as how can ana employee checkin in a day and checkout in another
        salary=hours_worked*salary_per_hour
        #batches cal
        batches=Batche.objects.filter(employee=emp)
        for batch in batches:
            salary=salary+(batch.size*batch.item_price)
        p=Payment(date=datetime.now(),employee=emp,amout=salary)
        # check if payment exits dunt save
        p.save()
        #cal payment



    # attendance=Attendance.objects.filter(employee=employee)
    # attendance_exptions=AttendanceException.objects.filter(attendance__in=[o.id for o in attendance])
    # attendance=Attendance.objects.filter(employee=employee).exclude(id__in=[o.attendance.id for o in attendance_exptions])
    # final_attendace=list(chain(attendance, attendance_exptions))
    # return final_attendace
    


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

    def __unicode__(self):
        s=self.identifier+"-"+self.description+"-"+str(self.value)
        return s

#Batches: ID, Employee ID, Date, item ID, Piece price, Size
class Batch(models.Model):
    employee = models.ForeignKey(Employee)
    date = models.DateTimeField(default=datetime.datetime.now())
    item = models.ForeignKey(Item)
    item_price = models.IntegerField()
    size = models.IntegerField(default=0)
    reason = models.CharField(max_length=100,default="none")  

    def __unicode__(self):
        s=self.employee.name+"-"+str(self.item)+"-"+str(self.item_price)
        return s
#Payment: ID, Date, Employee ID, amount
class Payment(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    employee = models.ForeignKey(Employee)
    amount = models.IntegerField()

    def __unicode__(self):
        s=self.employee.name+"-"+self.amount+"-"+self.date
        return s
#Loans: ID, Date, Employee ID, Amount
class Loan(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    employee = models.ForeignKey(Employee)
    amount = models.IntegerField()
    def __unicode__(self):
        return self.employee.name + str("__") + str(self.amount)
##