#! /user/bin/python3


def amino_acid(protein,residue):
	length=len(protein)
	res=protein.upper().count(residue)
	percentage=100*(res/length)
	return percentage

print(amino_acid("MSRSLLLRFLLFLLLLPPLP","L"))

