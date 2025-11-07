#! /bin/user/python3

seqs= ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

seq= list(range(0,len(seqs)))

for X in seq:
	first=list(seqs[X])
for Y in seq:
	distance=0
	second=list(seqs[Y])
	
	for base in list(range(0,len(first))):
		print(str(first)+ "," + str(second))
		if first[base]==second[base]:
			distance=distance+1
		else:
			print(str(distance) + "identity" + seqs[X] + "and" + seqs[Y])
			
			print(str(int(100*(distance/len(seqs[X])))))


