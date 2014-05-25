'''			
'''
import study_groups_reducer
import unittest
import csv

class mapper_study_groups_test(unittest.TestCase):
	
	fileLocation = './reducer_test_data.txt'

	def test(self):
		result = study_groups_reducer.reducer(open(self.fileLocation))
		
		#with open(self.fileLocation) as csvfile:
		#	reader = csv.reader(csvfile, delimiter='\t')
		#	result = study_groups_reducer.reducer(reader)