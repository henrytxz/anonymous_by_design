#!/usr/bin/env python

import sys

def reducer (reader):
	
	'''
	We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.
	
	As the first step for this analysis we have been tasked with writing a map reduce program that for each forum thread (that is a question node with all it's answers and comments) 
	would give us a list of students that have posted there - either asked the question, answered a question or added a comment. 
	
	If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
	
	Key question_id, value author_id
	'''
	
	result = {} # the key of this dictionary will be question_ids and value list of author_ids  

	for line in reader:
		data = line.strip().split()
		if len(data)!=2:
			continue
		question_id, author_id = data
		
		if question_id in result:
			result[question_id].append(author_id) 
		else:
			result[question_id] = [author_id]
			
	for key, value in result.iteritems():
		print key, '\t', value

				
if __name__ == "__main__":
	reducer(sys.stdin)