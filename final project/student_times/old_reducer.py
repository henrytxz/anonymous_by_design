#!/usr/bin/env python

import sys
import csv

def reducer():
	lineCount=0
	maxHrCount=0
	currHrCount=0
	for line in stdin:
		author=line.strip().split()[0]
		if lineCount==0:
			oldAuthor = author
			lineCount+=1
		hr=line.strip().split()[1]

		if author!=oldAuthor:
			for i in mostActiveHr:
				print author+" "+mostActiveHr[i]
			oldAuthor=author
			maxHrCount=0
			currHrCount=0
		else:
			if maxHrCount==0:
				mostActiveHr.append(hr)
				maxHrCount+=1
				currHrCount+=1
			elif
				
		
		
