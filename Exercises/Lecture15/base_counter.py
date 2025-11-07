#! /user/bin/python3

def base_counter(dna,bases):
	seq=len(dna)
	base=['A','T','G','C']
	for b in bases:
		dna_bases=dna.count(str(b))
	dna_unwanted=seq-dna_bases
	ratio=0.25*int(seq)
	if dna_unwanted > ratio:
		print("This sequence has" + str(dna_unwanted) + "bases")
	return dna_unwanted
print(base_counter("ATGCATCATG",['C','A']))

