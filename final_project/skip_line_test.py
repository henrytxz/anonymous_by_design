'''
testing the following:
1. case_node_is_question inserts correct question_id, question_len, number_of_ans==0 and ans_len_sum==0 
   if seeing the question_id before an ans
2.
				
'''
from final_project import skip_line
import unittest
import csv

class skip_line_test(unittest.TestCase):
	
	def test(self):
		line = ['id', 'title', 'tagnames', 'author_id', 'body', 'node_type', 'parent_id']
		skip_line.skip_line(line, 19)

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()