def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        
        # YOUR CODE HERE
        body = line[4]
        minusLastChar = body.strip('"')[:-1]
        punctuations = minusLastChar.count(".")+minusLastChar.count("!")+minusLastChar.count("?") 
        if punctuations < 1:
            writer.writerow(line)
