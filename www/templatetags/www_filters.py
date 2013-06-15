from django import template
from datetime import date, timedelta
import calendar
register = template.Library()
@register.filter
def month_name(date):
    return calendar.month_name[date.month]+str(" - ")+str(date.year)

@register.filter
def list_length(inlist):
	return len(inlist)