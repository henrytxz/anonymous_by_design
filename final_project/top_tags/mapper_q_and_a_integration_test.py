'''
'''

from top_tags.mapper_top_tags import py
import unittest
import csv

class mapper_q_and_a_integration_test(unittest.TestCase):
	fileLocation = '../testing/post_and_answer_length/data/test_data.txt'
	def test_integration(self):
		print "integration test:"
		with open(self.fileLocation) as csvfile:
			reader = csv.reader(csvfile, delimiter='\t')
			result = py.mapper(reader)
			self.assertTrue(result.has_key(5339))
			self.assertTrue(result.has_key(2312))
			self.assertTrue(result.has_key(1234))
			
			value5339 = result[5339]
			self.assertEqual(10, value5339[0])	#body of the question is 'empty body'
			self.assertEqual(0, value5339[1])	#0 ans node
			self.assertEqual(0, value5339[2])
			
			value2312 = result[2312]
			self.assertEqual(133, value2312[0])
			self.assertEqual(1, value2312[1])	#1 ans node
			self.assertEqual(38, value2312[2])	#body of the ans is 'body: answer whose question_id_in_dict' 

			value1234 = result[1234]
			self.assertEqual(25, value1234[0])
			self.assertEqual(2, value1234[1])	#1 ans node
			self.assertEqual(12, value1234[2])	#body of the ans is 'body'
