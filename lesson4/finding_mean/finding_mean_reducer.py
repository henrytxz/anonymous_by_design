#!/usr/bin/env python
import sys

sum=0.0
nbrSales=0

for line in sys.stdin:
	data = line.split()
	if (len(data)!=2):
		print "warning! " + line 
		continue
	
	date,cost = data
	sum+=float(cost)
	nbrSales+=1

print sum/nbrSales

		
