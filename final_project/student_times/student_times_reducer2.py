#!/usr/bin/env python

import operator
import sys
from processAuthor import processAuthor
from processHr import processHr

def initVars():
	return [0,[],0,0,None,None]

def initOldAuthor(lineCount,author,hr):
	lineCount+=1
	return [lineCount,author,hr]

def reducer(f):
	#lineCount,maxHr,maxHrCount,currHrCount,oldAuthor,author = initVars()
	
	student_dict = {}
	
	for line in f: 
		data = line.strip().split()
		if len(data)!=2:
			continue
		author,hr = data
		
		if author in student_dict:
			if hr in student_dict[author]:
				student_dict[author][hr] = student_dict[author][hr]+1
			else:
				student_dict[author][hr] = 1
		else:
			student_dict[author] = {hr:1}

		#if lineCount==0:
		#	lineCount,oldAuthor,oldHr = initOldAuthor(lineCount,author,hr)

		#oldAuthor,maxHr,maxHrCount,currHrCount,oldHr = processAuthor(oldAuthor,author,maxHr,maxHrCount,currHrCount,oldHr,hr)
		
		#if currHrCount!=0: #only 0 right after seeing a new author
		#	oldHr,maxHr,maxHrCount,currHrCount = processHr(oldHr,hr,maxHr,maxHrCount,currHrCount)
		
		#currHrCount+=1		
		
	#processAuthor(oldAuthor,'',maxHr,maxHrCount,currHrCount,oldHr,hr)
	
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
	
	#reverse_dict = {}
	#for key, value in d.iteritems():
	#	reverse_dict[value] = key
	
	#sorted_d = sorted(reverse_dict.iteritems(), key=operator.itemgetter(1), reverse=True)	
	sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)
	maxHrFreq = None
	
	for a_tuple in sorted_d:
		if not result:
			maxHr 	  = a_tuple[0]
			maxHrFreq = a_tuple[1]
			result.append(maxHr)	#sorted_d is sorted in reverse order => the 1st is definitely a max
		elif a_tuple[1]<maxHrFreq:		#found an hr that is not as frequent as the max hr so stop
			break
		else:							#found an hr that is as frequent as the max hr so append
			result.append(a_tuple[0])		
		 
	#print sorted_d
	return result

if __name__ == "__main__":
	reducer(sys.stdin)



