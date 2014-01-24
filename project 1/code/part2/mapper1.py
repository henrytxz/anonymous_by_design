#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split()
    #print len(data)
    if len(data) == 10:
        IP,id,username,time,timeZone,method,page,protocol,status,objectSize = data
        print "{0}".format(page)

