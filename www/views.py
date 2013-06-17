# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse(" <a href='/admin'>Click here to got o the admin page</a>")

def import_attendance(request):
    return HttpResponse(" <h1>Welcome to the Attendance upload page</h1> ")

def view_reports(request):
    return HttpResponse(" <h1>Welcome to thereports page</h1> ")


def company_wide_salary_report(request):
	desired_year = request.POST['year']
	yearly_payments = Payment.objects.filter(date = desired_year)
	
	Jan = 0 
	Feb = 0 
	March = 0 
	April = 0 
	May = 0 
	June = 0 
	July = 0 
	August = 0 
	September = 0 
	October = 0 
	November = 0 
	December = 0 

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
	desired_year = request.POST['year']
	total_batches = len(Batch.objects.filter(date = year))
	total_items = len(Item.objects.filter(date = year))

	return render({'Total Batches': total_batches, 'Total Items': total_items})

def company_wide_output_monthly_report(request):
	desired_year = request.POST['year']
	desired_month = request.POST['month']
	total_batches = len(Batch.objects.filter(date = year w month))
	total_items = len(Item.objects.filter(date = year w month))

	return render({'Total Batches': total_batches, 'Total Items': total_items})

