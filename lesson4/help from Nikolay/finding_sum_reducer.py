#!/usr/bin/env python
import sys

sums=[0]*7
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data)!=2:
		continue
	weekday,sale=data
	sums[int(weekday)]+=float(sale)

for i in [0,1,2,3,4,5,6]:
	print "{0}\t{1}".format(i,sums[i])

#	print i + " " + float(sums[i])
