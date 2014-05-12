#!/usr/bin/env python

#import sys

def skip_line(line, expected_number_of_columns):
	
	if len(line)!=expected_number_of_columns:
		return True
	if line[0]=='id':
		return True
		

