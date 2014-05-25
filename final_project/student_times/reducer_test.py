'''
'''

import student_times_reducer
import unittest

class mapper_top_tags_test(unittest.TestCase):
	
	def test_findMaxHr(self):
		'''
		tests that student_times_reducer.findMaxHr returns empty list if given empty dict
		tests that student_times_reducer.findMaxHr does find the max hr when there is a few 
		'''		
		######################################################
		
		self.assertFalse(student_times_reducer.findMaxHr({}))
		
		######################################################
		# for author 100000066 
		d = {'01': 1, '05': 2}
		self.assertEqual(['05'], student_times_reducer.findMaxHr(d))
		
		d = {'01': 1, '05': 1}
		self.assertEqual(2, len(student_times_reducer.findMaxHr(d)))
		self.assertTrue('01' in student_times_reducer.findMaxHr(d))
		self.assertTrue('05' in student_times_reducer.findMaxHr(d))	
		

	#def test1(self):
		#fileLocation = './testing/student_test_posts_debug0.txt'
	#	fileLocation = './testing/student_test_posts_debug.txt'
	#	f=open(fileLocation, 'r')
	#	student_times_reducer.reducer(f)
