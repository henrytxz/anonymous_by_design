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

    #if len(data_mapped) == 1:
    #	thisSale = data_mapped[0]
	#print "thisSale:",thisSale
#	salesTotal += float(thisSale)
#	salesCount += 1
 
    thisPage = data_mapped[0]

    if oldPage and oldPage != thisPage:
    #    print oldPage, "\t", hitsCount 

	if hitsCount > mostPopPageHits:
		mostPopPage = oldPage
		mostPopPageHits = hitsCount

        oldPage = thisPage;
        hitsCount  = 0

    oldPage = thisPage
    hitsCount += 1

if mostPopPage != None:
    print mostPopPage, "\t", mostPopPageHits 

