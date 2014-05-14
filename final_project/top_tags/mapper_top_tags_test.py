'''
testing the following:
1. case_node_is_question inserts correct question_id, question_len, number_of_ans==0 and ans_len_sum==0 
   if seeing the question_id before an ans

todo: to finish documenting
2.
				
'''
import mapper_top_tags
import unittest
import csv

class mapper_top_tags_test(unittest.TestCase):
	
	
	fileLocation = '../testing/top_tags/test_data.txt' 
	with open(fileLocation) as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		reader.next()	#line 1: column headers
		question5339 			 = reader.next()	#line 2
		question1234 			 = reader.next()	#line 3
		ans_for_question1234 	 = reader.next()	#line 4
		comment_for_question1234 = reader.next()	#line 5
		
		#ans_whose_question_id_may_be_in_dict = reader.next()	#line 4
		#ans_non_int_question_id = reader.next()		#line 5
		#ans_negative_question_id = reader.next()	#line 6
	
	#def test_integration(self):	todo: solve ValueError: I/O operation on closed file
	#	print "integration test:"
	#	result = mapper_top_tags.mapper(self.reader)
	#	print result
	#	print '-'*70
	
	def test1(self):
		print 'test1:'
		#d = {}
		
		fileLocation = '../testing/top_tags/test_data.txt' 
		with open(fileLocation) as csvfile:
			reader = csv.reader(csvfile, delimiter='\t')
			d = mapper_top_tags.mapper(reader)
		
			#mapper_top_tags.case_node_is_question(d, self.question5339)
			self.assertTrue(d.has_key('cs101'))
			self.assertTrue(d.has_key('pdf'))
			self.assertTrue(d.has_key('cs387'))
			self.assertTrue(d.has_key('production'))
			self.assertTrue(d.has_key('audio'))
			print '-'*70
