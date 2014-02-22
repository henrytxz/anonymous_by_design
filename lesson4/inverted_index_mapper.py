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
        #print "line:"
	#print  line
	body = line[4]
        #print "body:"
	#print  body
	
	data = body.split()
	#data = body.split("\s.!?:;\"()<>[]#$=-/")
	print data
	print len(data)

	print strip_punctuation(body)

#        minusLastChar = body.strip('"')[:-1]
#        punctuations = minusLastChar.count(".")+minusLastChar.count("!")+minusLastChar.count("?") 
        #if punctuations < 1:
        #    writer.writerow(line)

mapper()
