'''
testing the following:

				
'''
import student_times_mapper
import unittest
import csv

class mapper_top_tags_test(unittest.TestCase):
	
	def test(self):
		fileLocation = '../testing/shared_data/student_test_posts_debug.csv'
		
		with open(fileLocation) as csvfile:
			reader = csv.reader(csvfile, delimiter='\t')
			student_times_mapper.mapper(reader)
			
			#for line in reader:
			#	print '-'*70
			#	print line
		
