#! /usr/bin/python3/

import os,subprocess,shutil

#reading in the local seqeunce and remote sequence

local_seq= open("plain_genomic_seq.txt").read().rstrip().upper()

remote_seq= open("lecture12new.fasta").read().rstrip().upper()

print (open("plain_genomic_seq.txt").read())

print (open("lecture12new.fasta").read())

#remove all non-protein related bases

local_seq_actual= local_seq.replace("X","").replace("K","").replace("S","").replace("L","")


#making coding and non-coding fragment

remote_seq_noncoding1 = remote_seq[0:28]

remote_seq_exon = remote_seq[28:409]

remote_seq_noncoding2 = remote_seq[409:]

local_seq_noncoding1 = local_seq[0:62]

local_seq_exon = local_seq[62:91]

local_seq_noncoding2 = local_seq[91:]

print (remote_seq_exon)

print (local_seq_exon)





