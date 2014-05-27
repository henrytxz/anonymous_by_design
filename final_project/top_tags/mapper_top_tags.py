#!/usr/bin/env python

import sys
import csv

#from final_project.skip_line import skip_line 	#this works in Eclipse but not Git Bash => just copy skip_line to the same folder and move on for now
from skip_line import skip_line 
#import final_project.skip_line

def mapper(reader):

	result = {}

	for line in reader:
		if skip_line(line, 19):
			continue
		else:
			node_type = line[5]
			
			if node_type == 'question': 
				case_node_is_question(result, line)
				
	for key, value in result.iteritems():  					
		print key, '\t', value			
	
	return result
	
def case_node_is_question(dictionary, line):
		tagnames = line[2].split()
		for tag in tagnames:
			if tag in dictionary:
				dictionary[tag] = dictionary[tag]+1
			else:
				dictionary[tag] = 1 
				
if __name__ == "__main__":
	reader = csv.reader(sys.stdin, delimiter='\t')
	mapper(reader)