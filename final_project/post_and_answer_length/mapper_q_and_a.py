#!/usr/bin/env python

import sys
import csv

import skip_line

def mapper(reader):
	#reader = csv.reader(sys.stdin, delimiter='\t')

	result = {}

	for line in reader:
		#print len(line)
		if skip_line(line, 19):
		#if False:
			continue
		else:
			node_type = line[5]
			#print node_type
			
			if node_type == 'question': 
				case_node_is_question(result, line)
					
			if node_type == 'answer':
				print "node_type is answer"
				question_id = line[6]
				if bad_question_id(question_id):
					continue				
				if question_id in result:				
					case_node_is_answer_and_question_id_in_dictionary(result, line, question_id)
				else:
					case_node_is_answer_and_question_id_not_yet_in_dictionary(result, line)					
	
	#print '-'*60			
	print result
	
def case_node_is_question(dictionary, line):
		question_id = int(line[0])
		question_len = len(line[4])
		number_of_ans = 0
		ans_len_sum = 0
		dictionary[question_id] = [question_len, number_of_ans, ans_len_sum]

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
	mapper()