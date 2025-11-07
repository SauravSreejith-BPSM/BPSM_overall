#! /user/bin/python3

def kmer(dna,size=2,freq=2):
	dna=dna.upper()
	kmers=[]
	ranges=list(range(0,len(dna)))
	for start in ranges:
		if (start+size) < len(dna)+1:
			output=(dna)[start:start+size]
			found=kmers+[output]
	return found

print(kmer('atatatatatcgcgtatatatacgactatatgcattaattatagcatatcgatatatatatcgatattatatcgcattatacgcgcgtaattatatc',2,2))


			
