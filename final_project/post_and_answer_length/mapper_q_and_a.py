#!/usr/bin/env python

import sys
import csv
import os

from skip_line import skip_line

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')

	for line in reader:
		if skip_line(line):
			continue
		else:
			print "node_type: %s" % line[5]
		
mapper()