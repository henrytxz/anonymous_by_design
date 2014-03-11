#!/usr/bin/env python

import sys
import string
from datetime import datetime
from weekdaySwitch import weekdaySwitch
#from isMonday import isMonday
#from isSunday import isSunday

#d={}

for line in sys.stdin:
	data = line.split('\t')
	date,time,store,item,cost,payment = data
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

	print weekday + " " + cost
	#print weekdaySwitch(weekday) + " " + cost



#	d[date]=''

#	if isSunday(date):
#		print date + " " + cost

