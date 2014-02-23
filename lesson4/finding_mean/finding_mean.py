#!/usr/bin/env python

import sys
import string

d={}

for line in sys.stdin:
	data = line.split('\t')
	date,time,store,item,cost,payment = data
	d[date]=''

for key in d.keys():
	print key
