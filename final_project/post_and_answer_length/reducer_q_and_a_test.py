'''			
'''
import mapper_q_and_a
import unittest
import csv
import subprocess

class reducer_q_and_a_test(unittest.TestCase):
	
	returncode = subprocess.call(["ls", "-l"])
	
	#I haven't gotten the above idea to work on Windows 7 yet
	#but ran
	#cat ../testing/shared_data/bigger_node_test.txt | mapper_q_and_a.py | sort | reducer_q_and_a.py | wc -l
	#while in ~/Documents/GitHub/foo/final_project/post_and_answer_length
	#and result looks ok