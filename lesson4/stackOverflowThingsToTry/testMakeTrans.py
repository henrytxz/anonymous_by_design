#!/usr/bin/env python

from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "$2345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab);
