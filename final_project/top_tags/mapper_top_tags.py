#!/usr/bin/env python

import sys
import csv

import skip_line

def mapper(reader):
	#print reader

	result = {}

	for line in reader:
		#print line
		#print len(line)
		if skip_line.skip_line(line, 19):
			continue
		else:
			node_type = line[5]
			
			if node_type == 'question': 
				case_node_is_question(result, line)
					
			if node_type == 'answer':
				continue
				question_id = line[6]
				if bad_question_id(question_id):
					continue
				question_id = int(question_id)
				if question_id in result:				
					case_node_is_answer_and_question_id_in_dictionary(result, line)
				else:
					case_node_is_answer_and_question_id_not_yet_in_dictionary(result, line)		
				
	#for key, value in result.iteritems():  					
	#	print key, '\t', str(value[0])+','+str(value[1])+','+str(value[2])			
	
	return result
	
def case_node_is_question(dictionary, line):
		#question_id = int(line[0])
		tagnames = line[2].split()
		for tag in tagnames:
			if tag in dictionary:
				dictionary[tag] = dictionary[tag]+1
			else:
				dictionary[tag] = 1 
		
		#question_len = len(line[4])
		#number_of_ans = 0
		#ans_len_sum = 0
		#if question_id in dictionary:
		#	number_of_ans = dictionary[question_id][1]
		#	ans_len_sum = dictionary[question_id][2]
		#dictionary[question_id] = [question_len, number_of_ans, ans_len_sum]

def case_node_is_answer_and_question_id_in_dictionary(dictionary, line):
		question_id = int(line[6])
		value = dictionary[question_id]	#print value
		question_len = value[0]
		number_of_ans = value[1]+1
		ans_len_sum = value[2]+len(line[4])
		dictionary[question_id] = [question_len, number_of_ans, ans_len_sum]	

def case_node_is_answer_and_question_id_not_yet_in_dictionary(dictionary, line):
		question_id = int(line[6])
		question_len = 0
		number_of_ans = 1
		ans_len_sum = len(line[4])
		dictionary[question_id] = [question_len, number_of_ans, ans_len_sum]		
	
def bad_question_id(question_id):
	return question_id.isdigit() == False	#this takes out letters and negative numbers ('-' is not a digit)
		
if __name__ == "__main__":
	reader = csv.reader(sys.stdin, delimiter='\t')
	mapper(reader)