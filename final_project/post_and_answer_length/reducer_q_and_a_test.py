'''	
	#I haven't gotten the subprocess idea to work on Windows 7 yet
	#so instead I ran
	#cat ../testing/shared_data/bigger_node_test.txt | mapper_q_and_a.py | sort | reducer_q_and_a.py | wc -l
	#while in ~/Documents/GitHub/foo/final_project/post_and_answer_length
	#and result looks ok		
'''
#import mapper_q_and_a
import unittest
#import csv
import subprocess

class reducer_q_and_a_test(unittest.TestCase):
	
	#14 May 2014: not sure why this is not working :(
	#http://stackoverflow.com/questions/17374287/subprocess-error-dealing-with-ls-argument-in-call-function
	#says it should work
	
	#returncode = 
	subprocess.call(["dir", "/w"])	
	
	#returncode = 
	#subprocess.call(["ls", "-l"])
	
	#subprocess.call(['ipconfig', '/all'])
	
