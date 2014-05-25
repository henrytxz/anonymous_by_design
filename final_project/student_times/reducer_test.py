'''
testing the following:

				
'''
import student_times_reducer
import unittest
import csv

class mapper_top_tags_test(unittest.TestCase):
	
	def test(self):
		fileLocation = './testing/student_test_posts_debug.txt'
		
		f=open(fileLocation, 'r')
		student_times_reducer.reducer(f)
		
