def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    count = 1
    
    #for line in reader:
    for line in sys.stdin:
        # YOUR CODE HERE
            
        #if count ==3:    
        #writer.writerow(line)
        #count = count+1
        
        data = line.strip().split("\t")
        if len(data) == 6:
            f1, f2, f3, f4, body, f6 = data
            #print body.find(".")
            minusLastChar = body.strip('"')[:-1]
            #print body
            punctuations = minusLastChar.count(".")+minusLastChar.count("!")+minusLastChar.count("?") 
            if punctuations < 1:
                print body
