'''			
'''
import mapper_q_and_a
import unittest
import csv
import subprocess

class reducer_q_and_a_test(unittest.TestCase):
	
	returncode = subprocess.call(["ls", "-l"])
	
	
	
	
	fileLocation = '../testing/post_and_answer_length/data/data_test_node_type_ans_yet_key_not_found.txt' 
	
	with open(fileLocation) as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		reader.next()	#line 1: column headers
		question5339 = reader.next()	#line 2
		question2312 = reader.next()	#line 3
		ans_whose_question_id_may_be_in_dict = reader.next()	#line 4
		ans_non_int_question_id = reader.next()		#line 5
		ans_negative_question_id = reader.next()	#line 6

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()