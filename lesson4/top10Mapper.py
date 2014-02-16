#!/usr/bin/python
import sys
import csv


#def mapper():

if 1:
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL)

    #result = sorted(reader, key=lambda
    
    l = list()
    #listOfLines = list()
    dict = {}
    
    for line in reader:
        # YOUR CODE HERE
        body = line[4]
        l.append(body)
        #listOfLines.append(line)
        dict[line[4]] = line
    
    l2 = sorted(l, key=len, reverse=True)[0:10]
    #print l2    
    #print dict
    
    l3 = sorted(l2, key=len)
    #print l3
    #print len(l3)
    
    for body in l3:
        print dict[body]
        #val = "\"\t\"".join((dict[body]))
        #print('"'+val+'"')
        #print writer.writerow(dict[body])
        #print "done"
    
#    for line in reader:
 #           print line
    
  #  sys.stdin.seek(0)
   # for line in reader:
    #        print line[4]
