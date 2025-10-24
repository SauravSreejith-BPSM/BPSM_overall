
#!/usr/bin/python3

#question1

DNAinitial = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#counting A

countA = DNAinitial.count("A")

#counting T

countT = DNAinitial.count("T")

#calculating A-T enrichment

length = len(DNAinitial)

AT = ((countA + countT)/length)*100

print("Total A and T concentration is" + str(AT))


#question2

DNAagain = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#replacing individually

DNA1 = DNAagain.replace("A","t")
DNA2 = DNA1.replace("G","c")
DNA3 = DNA2.replace("C","g")
DNAFinal = DNA3.replace("T","a")
DNAFinal = DNAFinal.upper()

print("Complement sequence is" + "DNAFinal")


#question3

DNA3 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#finding position

Motif = DNA3.find("GAATTC")

print(Motif)

#lengths of fragments

Fragments = DNA3.find("GAATTC") + 1

print(Fragments)

Second = len(DNA3) - Fragments

print(Second)

#question4

Genomic= "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
Exon1 = Genomic[0:63]
print(Exon1)
Exon2 = Genomic[91:]
print(Exon2)
Coding = Exon1 + Exon2
print(Coding)
