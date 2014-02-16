#!/usr/bin/python

import sys
import string

def strip_punctuation(s):
	table = string.maketrans("","")
	result = s.translate(table, string.punctuation)
	print result
	return result

#strip_punctuation(sys.stdin.read())
#strip_punctuation("<p> ca")

