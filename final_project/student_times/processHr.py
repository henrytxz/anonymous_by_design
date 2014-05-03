#!/usr/bin/env python

import sys
import csv

def processHr(oldHr,hr,maxHr,maxCount,currHrCount):
	#print "{0} {1} {2} {3} {4}".format(oldHr,hr,maxHr,maxCount,currHrCount)
	if hr!=oldHr:
		if currHrCount>maxCount:
			maxHr=[oldHr]
			maxCount=currHrCount
		elif currHrCount==maxCount:
			maxHr.append(oldHr)
#			print "{0} {1} {2} {3} {4}".format(oldHr,hr,maxHr,maxCount,currHrCount)
		oldHr=hr
		currHrCount=0
	return [oldHr,maxHr,maxCount,currHrCount]
