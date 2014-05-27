#!/usr/bin/env python

import sys
import operator

'''
Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in. 
'''

def reducer():

	d = {}
		
	for line in sys.stdin:
		data_mapped = line.strip().split("\t")
		if len(data_mapped) != 2:
			# Something has gone wrong. Skip this line.
			continue
		
		tag, numberAppearanceStr = data_mapped
		numberAppearance = int(numberAppearanceStr)
		if tag in d:
			d[tag] = d[tag]+numberAppearance
		else:
			d[tag] = numberAppearance
	
	#creates a list, key=operator.itemgetter(1) will sort by value
	#if one wants to sort by key, you'd use key=operator.itemgetter(0)
	#set reverse=True because I want descending order in frequency
	sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)
		
	top10 = sorted_d[:10]	
		
	for a_tuple in top10:
		print a_tuple[0], '\t', a_tuple[1]	
			

if __name__ == "__main__":
	reducer()

