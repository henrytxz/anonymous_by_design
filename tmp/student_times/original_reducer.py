#!/usr/bin/env python

import sys
import csv
import fileinput
from processAuthor import processAuthor
from processHr import processHr

def initVars():
	return [0,[],0,0,None,None]

def initOldAuthor(lineCount,author,hr):
	lineCount+=1
	return [lineCount,author,hr]

def reducer():
	lineCount,maxHr,maxHrCount,currHrCount,oldAuthor,author = initVars()
	for line in sys.stdin:
		data = line.strip().split()
		if len(data)!=2:
			continue
		author,hr = data

		if lineCount==0:
			lineCount,oldAuthor,oldHr = initOldAuthor(lineCount,author,hr)

		oldAuthor,maxHr,maxHrCount,currHrCount,oldHr = processAuthor(oldAuthor,author,maxHr,maxHrCount,currHrCount,oldHr,hr)
		
		if currHrCount!=0: #only 0 right after seeing a new author
			oldHr,maxHr,maxHrCount,currHrCount = processHr(oldHr,hr,maxHr,maxHrCount,currHrCount)
		
		currHrCount+=1		
		
	processAuthor(oldAuthor,author,maxHr,maxHrCount,currHrCount)	
		
#########################################################################
#f=open('./debugInput.txt', 'r')
reducer()




