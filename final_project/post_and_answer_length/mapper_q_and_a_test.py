'''
testing the following:
1. case_node_is_question inserts correct question_id, question_len, number_of_ans==0 and ans_len_sum==0 
   if seeing the question_id before an ans
2.
				
'''
import mapper_q_and_a
import unittest

class mapper_q_and_a_test(unittest.TestCase):
	try:
		f = open('../testing/post_and_answer_length/data/data_test_node_type_ans_yet_key_not_found.txt')
	except IOError:
		print "could not open file"
	
	f = open('../testing/post_and_answer_length/data/data_test_node_type_ans_yet_key_not_found.txt')
	f.next()	#line 1: column headers
	question_line0 = f.next()	#line 2	
	question_line = question_line0.split('\t') 
	f.next()	#line 3
	ans_line_question_id_in_dict = f.next()
	ans_line_non_int_question_id = f.next()
	ans_line_negative_question_id = f.next()
	ans_line_non_int_question_id = f.next()
	
	def test1(self):
			
#		print "file name:", f.name
#		print "try f.next()"
#		print f.next()
		
		d = {}
		mapper_q_and_a.case_node_is_question(d, self.question_line)
		print d
		self.assertTrue(d.has_key(5339))
		#value = d['5339']
		

#	def testName(self):
#		pass


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()