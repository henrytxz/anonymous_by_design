#!/usr/bin/env python

from datetime import date

def isMonday(d):
	data = d.split('-')
	year,month,day = data

	result = date(int(year),int(month),int(day))
	if result.weekday()==0:
		return True
	else:
		return False

## tests ############################################

#print isMonday('2014-02-24')
#print isMonday('2014-02-25')

#d = date(2014,2,24)
#print d.weekday()




