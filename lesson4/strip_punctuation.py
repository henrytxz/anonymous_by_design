#!/usr/bin/python

import sys
import string
from string import maketrans

def strip_punctuation(s):
	table = string.maketrans(string.punctuation,' '*len(string.punctuation))
	#table = string.maketrans("<",' ')
	#table = string.maketrans(".!?:;"()<>[]#$=-/", "                 ")
	result = s.translate(table, string.punctuation)
	return result


