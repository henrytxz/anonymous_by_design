#!/usr/bin/python

import sys

mostPopPage = None
mostPopPageHits = 0
oldPage = None
hitsCount = 0

# Loop around the data

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 1:
	print "len(data_mapped) not 1!"
	continue
 
    thisPage = data_mapped[0]

    if oldPage and thisPage!=oldPage:
	if hitsCount > mostPopPageHits:
		mostPopPage = oldPage
		mostPopPageHits = hitsCount
        hitsCount  = 0

    oldPage = thisPage
    hitsCount += 1

if mostPopPage != None:
    	if hitsCount > mostPopPageHits:
		mostPopPage = oldPage
		mostPopPageHits = hitsCount
	
	print mostPopPage, "\t", mostPopPageHits 

