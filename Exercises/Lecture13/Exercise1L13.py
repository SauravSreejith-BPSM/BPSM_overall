#! /user/bin/python3

input= open("input.txt").read().split()

adapter= open("cleaned.txt",'w')


for sequence in input:
  adapter.write(sequence[14:] + '\n')
  sequence[14:] 

print(open('cleaned.txt').read().rstrip())

#completed Exercise 1



