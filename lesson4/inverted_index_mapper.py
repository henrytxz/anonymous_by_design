#!/usr/bin/env python

import sys
import csv
import string

from strip_punctuation import strip_punctuation


def mapper():
    
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        
        # YOUR CODE HERE
	body = line[4]
	
	data = body.split()
	#data = body.split("\s.!?:;\"()<>[]#$=-/")
	print body 

#	print len(data)

	print strip_punctuation(body)


mapper()
