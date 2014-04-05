def reducer():

	salesTotal = 0
	oldKey = None
	
	for line in sys.stdin:
		data = line.strip().split("\t")

		if len(data) != 2:
			continue

		thisKey, thisSale = data

		if oldKey and oldKey != thisKey:	# oldKey is None before you read line 1
							# no point printing None

			print "{0}\t{1}".format(oldKey, salesTotal)

			salesTotal = 0

		oldKey = thisKey
		salesTotal += float(thisSale)

	if oldKey:
		print "{0}\t{1}".format(oldKey, salesTotal)

			
