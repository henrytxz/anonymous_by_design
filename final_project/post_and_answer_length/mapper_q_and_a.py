#!/usr/bin/env python

import sys
import csv
import os

#http://stackoverflow.com/questions/714063/python-importing-modules-from-parent-folder
#http://stackoverflow.com/questions/9271464/what-does-the-file-wildcard-mean-do
#parentDir = os.path.dirname(__file__)
#sys.path.insert(0, parentDir)

#from final_project 
from skip_line import skip_line

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')

	for line in reader:
		if skip_line(line):
			continue
		else:
			print "node_type: %s" % line[5]
		
mapper()