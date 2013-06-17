# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")


def company_wide_salary_report(request):
	desired_year = request.GET['year']
	yearly_payments = Payment.objects.filter(date__year = desired_year)
	
	Jan = Feb = March = April = May = June = July = August = September = October = November = December = 0  

	for payment in yearly_payments:
		if payment.date.Month = 1:
			Jan = Jan + payment.amount
		if payment.date.Month = 2:
			Feb = Feb + payment.amount
		if payment.date.Month = 3:
			March = March + payment.amount
		if payment.date.Month = 4:
			April = April + payment.amount
		if payment.date.Month = 5:
			May = May + payment.amount
		if payment.date.Month = 6:
			June = June + payment.amount
		if payment.date.Month = 7:
			July = July + payment.amount
		if payment.date.Month = 8:
			August = August + payment.amount
		if payment.date.Month = 9:
			September = September + payment.amount
		if payment.date.Month = 10:
			October = October + payment.amount
		if payment.date.Month = 11:
			November = November + payment.amount
		if payment.date.Month = 12:
			December = December + payment.amount
	
	Dict = {'Jan': Jan, 'Feb': Feb, 'March': March, 'April': April, 'May': May, 'June': June, 'July': July, 'August': August, 
	' September': September, 'October': October, 'November': November, 'December': December}

	return render(request, Dict)

def company_wide_output_yearly_report(request):
	desired_year = request.GET['year']
	total_batches = Batch.objects.filter(date__year = desired_year)
	number_of_employees = len(Employee.objects.all())

	Jan = Feb = March = April = May = June = July = August = September = October = November = December = 0

	for batches in total_batches:
		if batch.date.Month = 1:
			Jan = Jan + batch.size
		if batch.date.Month = 2:
			Feb = Feb + batch.size
		if batch.date.Month = 3:
			March = March + batch.size
		if batch.date.Month = 4:
			April = April + batch.size
		if batch.date.Month = 5:
			May = May + batch.size
		if batch.date.Month = 6:
			June = June + batch.size
		if batch.date.Month = 7:
			July = July + batch.size
		if batch.date.Month = 8:
			August = August + batch.size
		if batch.date.Month = 9:
			September = September + batch.size
		if batch.date.Month = 10:
			October = October + batch.size
		if batch.date.Month = 11:
			November = November + batch.size
		if batch.date.Month = 12:
			December = December + batch.size

	total_batches_size = Jan + Feb + March + April + May + June + July + August + September + October + November + December
	batch_per_employee = total_batches_size/number_of_employees

	Dict = {'Jan': Jan, 'Feb': Feb, 'March': March, 'April': April, 'May': May, 'June': June, 'July': July, 'August': August, 
	' September': September, 'October': October, 'November': November, 'December': December, 'batch_per_employee': batch_per_employee}

	return render(request, Dict)

def company_wide_output_monthly_report(request):
	desired_year = request.GET['year']
	desired_month = request.GET['month']
	total_batches = Batch.objects.filter(date__year = desired_year, date__month = desired_month)
	number_of_employees = len(Employee.objects.all())
	list_of_output_per_day = []
	for batches in total_batches:
		day = batches.date.day
		list_of_output_per_day[day] = list_of_output_per_day[day] + batches.size 


	number_of_items_in_list = len(list_of_output_per_day)
	list_of_output_per_day = range(number_of_items_in_list)
	total = sum(list_of_output_per_day) 
	batch_per_employee = total/number_of_employees

	Dict = {'number_of_items_in_list': number_of_items_in_list, 'batch_per_employee': number_of_items_in_list}

	return render(request, Dict)

def company_wide_output_monthly_report(request):
	desired_year = request.GET['year']
	desired_month = request.GET['month']
	total_batches = len(Batch.objects.filter(date = year w month))
	total_items = len(Item.objects.filter(date = year w month))

	return render({'Total Batches': total_batches, 'Total Items': total_items})

