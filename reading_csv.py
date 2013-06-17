# Full path and name to the csv file
csv_filepathname="/home/maii/Documents/read/payroll/www/attendace.csv"

# Full path to your django project directory

My_djangoproject="/home/maii/Documents/read/payroll/www"

import sys
from django.core.management import setup_environ
sys.path.append("/home/maii/Documents/read/payroll/www")

from payroll import settings

setup_environ(settings)

 


from www.models import MyCsvFile
import csv

dataReader = csv.reader(open('www/attendace.csv'), delimiter=',', quotechar='"')

for row in dataReader:
	

	if row[0] != 'Ac-No': # Ignore the header row, import everything else
		mycsv = MyCsvFile()
		mycsv.Ac_No = row[0]

		mycsv.name = row[1]
		print mycsv.name 
		mycsv.time = row[2]
		mycsv.finger_print= row[3]
		mycsv.machine = row[4]
		mycsv.save()