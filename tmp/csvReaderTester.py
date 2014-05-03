#!/usr/bin/env python

import sys
import csv

def reducer(): 
#	for line in sys.stdin:
	
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	for line in reader:
		if len(line)==6:
			nextLine=reader.next()
			if len(nextLine)==20:
				list = nextLine[2:5]
				list.append(nextLine[0]) 
				list = list+nextLine[6:11]+line[2:]
				print list 
		
#		writer.writerow(line)		


reducer()
