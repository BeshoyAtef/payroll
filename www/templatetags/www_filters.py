from django import template
from datetime import date, timedelta
import calendar
from www.models import Attendance

from django.contrib.humanize.templatetags.humanize import intword
register = template.Library()

@register.filter
def month_name(date):
    return calendar.month_name[date.month]+str(" - ")+str(date.year)

@register.filter
def list_length(inlist):
	return len(inlist)

@register.filter
def deduct(payment, deductions):
	return int(payment) - int(deductions)
@register.filter
def calculate_missing_days(attendance,employee):
    return attendance.filter(employee = employee).count() - attendance.filter(employee=employee).exclude(check_in__isnull=True).exclude(check_out__isnull=True).count()
@register.filter
def change_number(n):
    n3 = []
    r1 = ""
    # create numeric string
    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k
        # break if end of ns has been reached
        if q < -2:
            break
        else:
            if  q >= 0:
                n3.append(int(r[:3]))
            elif q >= -1:
                n3.append(int(r[:2]))
            elif q >= -2:
                n3.append(int(r[:1]))
        r1 = r
    
    #print n3  # test
    
    # break each group of 3 digits into
    # ones, tens/twenties, hundreds
    # and form a string
    nw = ""
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100)//10
        b3 = (x % 1000)//100
        #print b1, b2, b3  # test
        if x == 0:
            continue  # skip
        else:
            t = thousands[i]
        if b2 == 0:
            nw = ones[b1] + t + nw 
        elif b2 == 1:
            nw = tens[b1] + t + nw 
        elif b2 > 1:
            nw = twenties[b2] + ones[b1] + t + nw 
        if b3 > 0:
            nw = ones[b3] + "hundred " + nw 
    return nw

ones = ["", "one ","two ","three ","four ", "five ",
"six ","seven ","eight ","nine "]
tens = ["ten ","eleven ","twelve ","thirteen ", "fourteen ",
"fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]
twenties = ["","","twenty ","thirty ","forty ",
"fifty ","sixty ","seventy ","eighty ","ninety "]
thousands = ["","thousand ","million ", "billion ", "trillion ",
"quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ",
"nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
"quattuordecillion ", "sexdecillion ", "septendecillion ", "octodecillion ",
"novemdecillion ", "vigintillion "]
