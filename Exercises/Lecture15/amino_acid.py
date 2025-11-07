#! /user/bin/python3


def amino_acid(protein,res):
	length=len(protein)
	res=['A','I','L','M','F','W','Y','V']
	counter=0
	for aa in res:
		single=protein.upper().count(aa)
		counter=counter+single
	percentage=100*(counter/length)
	return percentage

print(amino_acid("MSRSLLLRFLLFLLLLPPLP",['M','L']))

