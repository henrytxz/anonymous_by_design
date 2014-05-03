#!/usr/bin/env python

#import sys

def skip_line(line):
	
	if len(line)!=19:
		return True
	if line[0]=='id':
		return True
		

