#! /bin/user/python3

import os,sys
import numpy as np
import matplotlib.pyplot as plt

ecoli_first = open("ecoli.txt").read().replace('\n','').upper()[0:50000]

window = 1000

a= []
t= []
g= []
c= []
at=[]

counter=0
for start in range(len(ecoli_first)-window):
	counter +=1
	win = ecoli_first[start:start+window]
	a.append(win.count('A')/window)
	t.append(win.count('T')/window)
	g.append(win.count('G')/window)
	c.append(win.count('C')/window)
	at.append((win.count('A')+win.count('T'))/window)

print(len(at))


ecoli_second = open("ecoli.txt").read().replace('\n','').upper()[0:100000]

a_a= []
t_t= []
g_g= []
c_c= []
at_at=[]

counter=0
for start in range(len(ecoli_second)-window):
        counter +=1
        win = ecoli_second[start:start+window]
        a_a.append(win.count('A')/window)
        t_t.append(win.count('T')/window)
        g_g.append(win.count('G')/window)
        c_c.append(win.count('C')/window)
        at_at.append((win.count('A')+win.count('T'))/window)

print(len(at_at))

ecoli_third = open("ecoli.txt").read().replace('\n','').upper()

a_final= []
t_final= []
g_final= []
c_final= []
at_final=[]

counter=0
for start in range(len(ecoli_third)-window):
        counter +=1
        win = ecoli_third[start:start+window]
        a_final.append(win.count('A')/window)
        t_final.append(win.count('T')/window)
        g_final.append(win.count('G')/window)
        c_final.append(win.count('C')/window)
        at_final.append((win.count('A')+win.count('T'))/window)

print(len(at_final))

plt.figure(figsize=(20,10))

plt.subplot(221)

plt.plot(at, label="AT content")

plt.ylabel('Content')

plt.xlabel('Position')

plt.title('AT content in 50000')

plt.legend()

plt.subplot(222)

plt.plot(at_at, label="AT content")

plt.ylabel('Content')

plt.xlabel('Position')

plt.axis([0,100000,0,1])

plt.title('AT content in 100000')

plt.legend()

plt.subplot(223)

plt.plot(at_final, label="AT content")

plt.ylabel('Content')

plt.xlabel('Position')

plt.axis([0,100000,0,1])

plt.title('AT content in genome')

plt.legend()

plt.savefig("Chart_02.png",transparent = True)

plt.show()

plt.close()

