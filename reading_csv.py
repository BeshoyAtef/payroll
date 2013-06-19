# Full path and name to the csv file
csv_filepathname="/home/maii/Documents/read/payroll/www/attendace.csv"

# Full path to your django project directory

My_djangoproject="/home/maii/Documents/read/payroll/www"

import sys
from django.core.management import setup_environ
sys.path.append("/home/maii/Documents/read/payroll/www")

from payroll import settings

setup_environ(settings)

 




from www.models import Attendance , Employee

import csv
import datetime

dataReader = csv.reader(open('www/attendace.csv'), delimiter=',', quotechar='"')

dic = {}
for row in dataReader:
	if row[0] != 'Ac-No': # Ignore the header row, import everything else
	    account_number = row[0]
	    stime = row[2]
	    if account_number not in dic:
	    	dic[account_number] = []

	    dic[account_number].append(stime)

for acc, stimes in dic.iteritems():
	
	checkin = stimes.pop(0)
	print checkin
	employee = Employee.objects.get(acc_no= acc)
	
	
	d = checkin[:-4].strip()
	check_in = datetime.datetime.strptime(d, "%m/%d/%Y %H:%M" )
	
	check_out = None
	for stime in stimes:
		
		stime = stime[:-4].strip()
		stime = datetime.datetime.strptime(stime, "%m/%d/%Y %H:%M" )
        
		if stime.date() == check_in.date():
			check_out = stime
			

		else:
			attend = Attendance()
			attend.check_in = check_in
			attend.check_out = check_out
			attend.employee = employee
			attend.save()
			check_in = stime
			check_out= None

			

