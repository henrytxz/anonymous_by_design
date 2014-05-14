'''
testing the following:

				
'''
import mapper_top_tags
import unittest
import csv

class mapper_top_tags_test(unittest.TestCase):
	
	def test1(self):
		print 'test1:'
		
		#fileLocation = '../testing/top_tags/test_data_reducer.txt' 
		fileLocation = '../testing/top_tags/doit/test_data_reducer.txt'
		
		with open(fileLocation) as csvfile:
			reader = csv.reader(csvfile, delimiter='\t')
			d = mapper_top_tags.mapper(reader)
		
			self.assertTrue(d.has_key('cs101'))
			self.assertTrue(d.has_key('pdf'))
			self.assertTrue(d.has_key('cs387'))
			self.assertTrue(d.has_key('production'))
			self.assertTrue(d.has_key('audio'))
			
			self.assertEqual(2, d['cs101'])
			self.assertEqual(1, d['pdf'])
			self.assertEqual(1, d['cs387'])
			self.assertEqual(1, d['production'])
			self.assertEqual(1, d['audio'])
