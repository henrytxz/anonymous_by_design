'''
testing the following:

				
'''
import student_times_reducer2
import unittest
import csv

class mapper_top_tags_test(unittest.TestCase):
	
	def test_findMaxHr(self):
		'''
		tests that student_times_reducer.findMaxHr returns empty list if given empty dict
		tests that student_times_reducer.findMaxHr does find the max hr when there is a few 
		'''		
		######################################################
		
		self.assertFalse(student_times_reducer2.findMaxHr({}))
		
		######################################################
		# for author 100000066 
		#d = {'01': 1, '05': 2}
		#self.assertEqual(['05'], student_times_reducer2.findMaxHr(d))
		
		d = {'01': 1, '05': 1}
		print student_times_reducer2.findMaxHr(d)
		#self.assertEqual(['05'], student_times_reducer2.findMaxHr(d))
		
		#fileLocation = './testing/student_test_posts_debug0.txt'
		
		#f=open(fileLocation, 'r')
		#d = student_times_reducer2.reducer(f)
		#print d
		
		

	#def test1(self):
		#fileLocation = './testing/student_test_posts_debug0.txt'
	#	fileLocation = './testing/student_test_posts_debug.txt'
	#	f=open(fileLocation, 'r')
	#	student_times_reducer2.reducer(f)
