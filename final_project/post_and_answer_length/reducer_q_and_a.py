#!/usr/bin/env python

import sys

'''
Write a map reduce program that would process the forum_node data and output the length of the post and the average answer 
(just answer, not comment) length for each post.
'''

def reducer():
	
	d = {}	
		
	for line in sys.stdin:
		data_mapped = line.strip().split("\t")
		if len(data_mapped) != 2:
			# Something has gone wrong. Skip this line.
			continue
		
		questionId, tripletStr = data_mapped 
		
		triplet = tripletStr.split(',')
		question_len 	= int(triplet[0])
		numberOfAns 	= int(triplet[1])
		sumOfAnsLength 	= int(triplet[2])
		
		if questionId in d:
			numberOfAnsSoFar 	= d[questionId][1]
			sumOfAnsLengthSoFar = d[questionId][2] 
			d[questionId] = [question_len, numberOfAnsSoFar+numberOfAns, sumOfAnsLengthSoFar+sumOfAnsLength]
		else:
			d[questionId] = [question_len, numberOfAns, sumOfAnsLength]
		
	#iterate through the dictionary whose key is questionId and value [question_len, numberOfAns, sumOfAnsLength]		
	for key, value in d.iteritems():
		questionId = key
		question_len 	= value[0]
		numberOfAns 	= value[1]
		sumOfAnsLength 	= value[2]
		aveAnsLength = calcAveAnsLength(numberOfAns, sumOfAnsLength)	
		
		print questionId, '\t', question_len, '\t', aveAnsLength
	
		
def calcAveAnsLength(numberOfAns, sumOfAnsLength):
	if numberOfAns == 0:
		return 0
	else:
		return float(sumOfAnsLength)/numberOfAns

if __name__ == "__main__":
	reducer()

