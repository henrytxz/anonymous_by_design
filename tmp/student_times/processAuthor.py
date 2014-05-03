#!/usr/bin/env python

import sys
import csv
from processHr import processHr

def processAuthor(oldAuthor,author,maxHr,maxHrCount,currHrCount,oldHr,hr):
	if author!=oldAuthor:
		oldHr,maxHr,maxHrCount,currHrCount = processHr(oldHr,hr,maxHr,maxHrCount,currHrCount)
		for i in maxHr:
			print oldAuthor+" "+i
		oldAuthor=author
		maxHr=[]
		maxHrCount=0
		currHrCount=0	
	return [oldAuthor,maxHr,maxHrCount,currHrCount,oldHr]
