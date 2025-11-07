#! /user/bin/python3

import os,subprocess,shutil

dna="ATGCATCATG"

k=1

n=list(range(1,2))

for window in n:
	kmers=[]
	range=list(range(0,len(dna)))
	for startingbase in range:
		if(startingbase+window)<len(dna)+1 :
			seqout=(dna)[startingbase:startingbase+window]
			kmers=kmers+[seqout]
			print(str(kmers) + "are the kmers")



