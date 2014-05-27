#!/usr/bin/env python

import sys
import csv

def mapper(reader):
	for line in reader:
	
		if len(line)!=19:
			continue
		if line[0]=='id':
			continue
		
		author_id=line[3]
		added_at =line[8]
	
		hour = added_at[11:13]
	
		print author_id+" "+hour

if __name__ == "__main__":
	reader = csv.reader(sys.stdin, delimiter='\t')
	mapper(reader)
