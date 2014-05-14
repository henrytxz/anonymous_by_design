#!/usr/bin/env python

import sys
import operator
#import csv
#import fileinput

'''Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in. 
'''

def reducer():

	d = {}
	#top10 = []
		
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
			
	sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)
		
	for a_tuple in sorted_d:
		print a_tuple[0], '\t', a_tuple[1]	
			
	#print '-'*70

if __name__ == "__main__":
	reducer()

