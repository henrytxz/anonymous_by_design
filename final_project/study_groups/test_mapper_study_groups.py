'''
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