#!/usr/bin/env python

from datetime import date

def isSunday(d):
	data = d.split('-')
	year,month,day = data

	result = date(int(year),int(month),int(day))
	if result.weekday()==6:
		return True
	else:
		return False

## tests ############################################

print isSunday('2014-03-09')

