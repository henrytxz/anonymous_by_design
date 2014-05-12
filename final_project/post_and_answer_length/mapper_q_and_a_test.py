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
	#try:
	#	f = open('../testing/post_and_answer_length/data/data_test_node_type_ans_yet_key_not_found.txt')
	#except IOError:
	#	print "could not open file"
	
	#question5339 = None
	
	fileLocation = '../testing/post_and_answer_length/data/data_test_node_type_ans_yet_key_not_found.txt' 
	
	with open(fileLocation) as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		reader.next()	#line 1: column headers
		question5339 = reader.next()	#line 2
		question2312 = reader.next()	#line 3
		ans_whose_question_id_may_be_in_dict = reader.next()	#line 4
		ans_non_int_question_id = reader.next()		#line 5
		ans_negative_question_id = reader.next()	#line 6
		
#	question_line0 = f.next()	#line 2	
#	question5339 = question_line0.split('\t') 
#	f.next()	#line 3
#	ans_line_question_id_in_dict = f.next()
#	ans_line_non_int_question_id = f.next()
#	ans_line_negative_question_id = f.next()
#	ans_line_non_int_question_id = f.next()
	
	def test1(self):
		print 'test1:'
		d = {}
		mapper_q_and_a.case_node_is_question(d, self.question5339)
		self.assertTrue(d.has_key(5339))
		value = d[5339]
		self.assertEqual(10, value[0])
		self.assertEqual(0, value[1])
		self.assertEqual(0, value[2])
		print '-'*70
		
	def test2(self):
		print "test2:"
		d = {}
		mapper_q_and_a.case_node_is_question(d, self.question2312)
		mapper_q_and_a.case_node_is_answer_and_question_id_in_dictionary(d, self.ans_whose_question_id_may_be_in_dict)
		self.assertTrue(d.has_key(2312))
		value = d[2312]
		self.assertEqual(133, value[0])
		self.assertEqual(1, value[1])
		#print len(self.ans_whose_question_id_may_be_in_dict[4])
		self.assertEqual(38, value[2])
		print '-'*70

	def test3(self):
		print "test3:"
		d={}
		mapper_q_and_a.case_node_is_answer_and_question_id_not_yet_in_dictionary(d, self.ans_whose_question_id_may_be_in_dict)
		self.assertTrue(d.has_key(2312))
		value = d[2312]
		self.assertEqual(0, value[0])
		self.assertEqual(1, value[1])
		self.assertEqual(38, value[2])
		print '-'*70
		
	def test_bad_input1(self):
		print "test_bad_input1:"
		self.assertTrue(mapper_q_and_a.bad_question_id(self.ans_non_int_question_id[6]))
		
	def test_bad_input2(self):
		print "test_bad_input2:"
		self.assertTrue(mapper_q_and_a.bad_question_id(self.ans_negative_question_id[6]))

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()