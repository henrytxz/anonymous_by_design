#!/usr/bin/env python

import sys
import string

for line in sys.stdin:	
        print line	
	#print line[4]
	table = string.maketrans(string.punctuation, "#"*len(string.punctuation))
	result = line.translate(table, string.punctuation)
	print "result:"+result

	table2 = string.maketrans('!','1')
	print "compromise:"+line.translate(table2, '!')

# test:

echo ! | script_strip_punctuation.py
