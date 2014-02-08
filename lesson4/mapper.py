def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    count = 1
    
    for line in reader:

        # YOUR CODE HERE
            
        if count ==3:    
            writer.writerow(line)

        count = count+1
