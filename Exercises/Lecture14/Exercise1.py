#!/user/bin/python3

import os,subprocess,shutil

data_gene_names = open('data.csv')


for geneline in data_gene_names:
	gene_info=geneline.split(",")
	species= gene_info[0]
	seqs=gene_info[1].upper()
	lengths=len(gene_info[1])
	names=gene_info[2]
	exp=int(gene_info[3])
	atcontent=(seqs.count('A')+seqs.count('T'))/lengths
	atstatus="low"
	if (atcontent>=0.45 and atcontent<=0.65):
		atstatus="medium"
	if (atcontent>0.65):
		atstatus="high"
	
	if species.endswith('melanogaster') or species.endswith('simulans'):
		print("These are the genes of interest "  + names)
	else:
		print("ommited")
	if lengths>90 and lengths<110:
		print("These are the sequences of interest" + names)
	else:
		print("ommited")
	if atcontent<0.5 and exp>200:
		print("These are genes of interest" + names)
	else:
		print("ommited")



