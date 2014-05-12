'''
testing the following:
1. case_node_is_question inserts correct question_id, question_len, number_of_ans==0 and ans_len_sum==0 
   if seeing the question_id before an ans
2.
				
'''
import mapper_q_and_a
import unittest
import csv

class mapper_q_and_a_test2(unittest.TestCase):
	try:
		f = open('../testing/post_and_answer_length/data/data_test_node_type_ans_yet_key_not_found.txt')
	except IOError:
		print "could not open file"
	
	question_line = None
	
	with open('../testing/post_and_answer_length/data/data_test_node_type_ans_yet_key_not_found.txt') as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		reader.next()	#line 1: column headers
		question_line = reader.next()
	
#	question_line0 = f.next()	#line 2	
#	question_line = question_line0.split('\t') 
#	f.next()	#line 3
#	ans_line_question_id_in_dict = f.next()
#	ans_line_non_int_question_id = f.next()
#	ans_line_negative_question_id = f.next()
#	ans_line_non_int_question_id = f.next()
	
	def test1(self):
		d = {}
		mapper_q_and_a.case_node_is_question(d, self.question_line)
		print d
		self.assertTrue(d.has_key(5339))
		value = d[5339]
		self.assertEqual(10, value[0])
		self.assertEqual(0, value[1])
		self.assertEqual(0, value[2])
		

#	def testName(self):
#		pass


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()