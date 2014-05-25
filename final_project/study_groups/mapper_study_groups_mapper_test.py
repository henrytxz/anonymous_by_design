'''
testing the following:
1. case_node_is_question inserts correct question_id, question_len, number_of_ans==0 and ans_len_sum==0 
   if seeing the question_id before an ans

todo: to finish documenting
2.
				
'''
import study_groups_mapper
import unittest
import csv

class mapper_study_groups_test(unittest.TestCase):
	
	fileLocation = '../testing/shared_data/student_test_posts.csv'

	def test_integration(self):
		print "integration test:"
		with open(self.fileLocation) as csvfile:
			reader = csv.reader(csvfile, delimiter='\t')
			result = study_groups_mapper.mapper(reader)