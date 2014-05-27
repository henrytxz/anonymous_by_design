#!/usr/bin/env python

import operator
import sys

def reducer(f):
	student_dict = {}
	
	for line in f: 
		data = line.strip().split()
		if len(data)!=2:
			continue
		author,hr = data
		
		#student_dict has author_id as keys and another dictionary as values
		#for eg: '100004819': {'10': 1, '04': 2, '05': 1}
		#		  100004819 is the author, [s]he was active once at 10, twice at 4 and once at 5
		if author in student_dict:	
			if hr in student_dict[author]:
				student_dict[author][hr] = student_dict[author][hr]+1
			else:
				student_dict[author][hr] = 1	
		else:
			student_dict[author] = {hr:1}
	
	print '-'*70
	print student_dict
	print '-'*70
	
	for key, value in student_dict.iteritems():
		l = findMaxHr(value)
		for hr in l:
			print key, '\t', hr 
		

def findMaxHr(d):
	result = []
	if not d:
		return result
	
	#creates a list, key=operator.itemgetter(1) will sort by value
	#if one wants to sort by key, you'd use key=operator.itemgetter(0)
	#set reverse=True because I want descending order in frequency
	#continue with the eg above, sorted_d would be [('04', 2), ('10', 1), ('05', 1)]
	sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)	
	
	maxHrFreq = None							   
	
	for a_tuple in sorted_d:
		if not result:
			maxHr 	  = a_tuple[0]
			maxHrFreq = a_tuple[1]
			result.append(maxHr)		#sorted_d is sorted in reverse order => the 1st tuple is definitely a max
		elif a_tuple[1] < maxHrFreq:	#found an hr that is not as frequent as the max hr => exit for loop
			break
		else:							#found an hr that is as frequent as the max hr so append
			result.append(a_tuple[0])		
		
	return result

if __name__ == "__main__":
	reducer(sys.stdin)



