#!/usr/bin/python

import sys

salesTotal = 0
salesCount = 0

# Loop around the data
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) == 1:
        thisSale = data_mapped[0]
        salesTotal += float(thisSale)
        salesCount += 1
    

print "salesTotal:",salesTotal,", salesCount:",salesCount
