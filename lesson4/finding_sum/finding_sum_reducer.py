#!/usr/bin/env python
import sys

sums=[0]*7
#print sums
for line in sys.stdin:
	data = line.split()
	weekday,sale=data
	sums[int(weekday)]+=float(sale)

print sums
