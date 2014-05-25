#!/usr/bin/env python

import sys
import csv

from skip_line import skip_line 

def mapper(reader):

	'''
	We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.
	
	As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) 
	would give us a list of students that have posted there - either asked the question, answered a question or added a comment. 
	
	If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
	
	Key question_id, value author_id?
	'''
	
	#print reader

	result = {}
	i=1

	for line in reader:
		#print line
		print str(i)+":"
		i+=1
		print len(line)

				
if __name__ == "__main__":
	reader = csv.reader(sys.stdin, delimiter='\t')
	mapper(reader)