#!/usr/bin/env python

import sys
import csv
from processAuthor import processAuthor
from processHr import processHr

# test new author
newOldAuthor,mostActiveHr,maxHrCount,currHrCount,oldHr = processAuthor('a1','a2',['08','09'],3,1,None,None)
if newOldAuthor=='a2' and not mostActiveHr and maxHrCount==0 and currHrCount==0:
        print "processAuthor test1 pass"
else:
	print "processAuthor test1 failed!"

# test same author
newOldAuthor,mostActiveHr,maxHrCount,currHrCount,oldHr = processAuthor('a1','a1',['08','09'],3,1,None,None)
if newOldAuthor=='a1' and mostActiveHr==['08','09'] and maxHrCount==3 and currHrCount==1:
        print "processAuthor test2 pass"
else:
	print "processAuthor test2 failed!"

# test new hour, not new max
newOldHr,maxHr,maxCount,currHrCount = processHr(8,9,[7],3,3)
if newOldHr==9 and maxHr==[7,8] and maxCount==3: #and currHrCount==0:
	print "processHr test1 pass"
else:
	print "processHr test1 failed! output:"
	print processHr(8,9,[7],3,3)

# test new hour, new max
newOldHr,maxHr,maxCount,currHrCount = processHr(8,9,[7],3,4)
if newOldHr==9 and maxHr==[8] and maxCount==4: 	 #and currHrCount==0:
	print "processHr test2 pass"
else:
	print "processHr test2 failed! output:"
	print processHr(8,9,[7],3,4)

# test same hour 
newOldHr,maxHr,maxCount,currHrCount = processHr('03','03',[],0,1)
if newOldHr=='03' and maxHr==[] and maxCount==0 and currHrCount==1:
	print "processHr test3 pass"
else:
	print "processHr test3 failed! output:"
	print processHr('03','03',[],0,1)
