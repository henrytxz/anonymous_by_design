#!/usr/bin/env python

import sys
import string
from isMonday import isMonday
from isSunday import isSunday

d={}

for line in sys.stdin:
	data = line.split('\t')
	date,time,store,item,cost,payment = data
#	d[date]=''

	if isSunday(date):
		print date + " " + cost

