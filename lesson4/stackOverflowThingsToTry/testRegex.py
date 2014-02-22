#!/usr/bin/python

import re

data = "Hey, you - what are you doing here!?"
print data.replace(",","").split() 

print re.findall(r"[\w']+", data)
