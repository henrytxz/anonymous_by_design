'''
	#I haven't gotten the subprocess idea to work on Windows 7 yet
	#but ran
	#cat ../testing/top_tags/test_data_reducer.txt | mapper_top_tags.py | sort | reducer_top_tags.py
	#while in ~/Documents/GitHub/foo/final_project/top_tags
	#and result looks good			
'''
#from top_tags.mapper_top_tags import py
import unittest
#import csv
import subprocess

class reducer_top_tags_test(unittest.TestCase):
	
	#returncode = subprocess.call(["ls", "-l"])
	
