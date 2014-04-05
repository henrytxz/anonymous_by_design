#!/usr/bin/env python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
	if len(line)==5:
		usr = line[0]
		if usr=='user_ptr_id':
			line.pop(0)
			line.insert(0,"0")
		line.insert(1,"A")
		writer.writerow(line)
	elif len(line)==19:
		author=line[3]
		if author=='author_id':
			author="0"
		line.pop(3)
		line.insert(0,"B")
		line.insert(0,author)
		writer.writerow(line)
	else:
		continue


mapper()
