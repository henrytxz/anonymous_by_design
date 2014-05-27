#!/usr/bin/env python

def skip_line(line, expected_number_of_columns):
	
	if len(line)!=expected_number_of_columns:
		return True		#skip bad rows
	if line[0]=='id':
		return True		#skip the row that consists of column headers
		

