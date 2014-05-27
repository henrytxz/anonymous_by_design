#!/usr/bin/env python

import sys
import csv

from skip_line import skip_line 

def mapper(reader):

	'''
	We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.
	
	As the first step for this analysis we have been tasked with writing a map reduce program that for each forum thread (that is a question node with all it's answers and comments) 
	would give us a list of students that have posted there - either asked the question, answered a question or added a comment. 
	
	If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
	
	Key question_id, value author_id
	'''
	
	for line in reader:
		if skip_line(line, 19):
			continue
		else:
			node_type = line[5]
			
			if node_type == 'question': 
				question_id = line[0]
				author_id 	= line[3]
			elif node_type == 'answer' or node_type == 'comment' :
				author_id 	= line[3]
				question_id = line[7]	#the abs_parent_id
				
			print question_id, '\t', author_id
				
				
if __name__ == "__main__":
	reader = csv.reader(sys.stdin, delimiter='\t')
	mapper(reader)