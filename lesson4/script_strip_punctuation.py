#!/usr/bin/env python

import sys
import string

for line in sys.stdin:	
	table = string.maketrans("","")
	result = line.translate(table, string.punctuation)
	print result


