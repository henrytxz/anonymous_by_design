#!/usr/bin/env python

import sys
#import csv
#import fileinput

'''Write a map reduce program that would process the forum_node data and output the length of the post and the average answer 
(just answer, not comment) length for each post. '''

def reducer():
	#d = {2312: [133, 1, 38], 1234: [25, 2, 12], 5339: [10, 0, 0]}
		
	for line in sys.stdin:
		data_mapped = line.strip().split("\t")
		if len(data_mapped) != 2:
			# Something has gone wrong. Skip this line.
			continue
		
		questionId, tripletStr = data_mapped 
		#print tripletStr
		
		triplet = tripletStr.split(',')
		#print triplet
		question_len = int(triplet[0])
		numberOfAns = int(triplet[1])
		sumOfAnsLength = int(triplet[2])
		aveAnsLength = calcAveAnsLength(numberOfAns, sumOfAnsLength)	#todo: 14 May 2014, this needs to be improved, what if there's more than 1 mapper? then the same question_id need
																		#					to be added before dividing
		
		print questionId, '\t', question_len, '\t', aveAnsLength
	
	#print '-'*70
		
def calcAveAnsLength(numberOfAns, sumOfAnsLength):
	if numberOfAns == 0:
		return 0
	else:
		return float(sumOfAnsLength)/numberOfAns

if __name__ == "__main__":
	reducer()

