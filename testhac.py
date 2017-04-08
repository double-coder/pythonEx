#!/bin/python3
#stma and ltma

import sys

stma=[]
ltma=[]
temp=0
n = int(input().strip())
p = list(map(int, input().strip().split(' ')))

for i in p:
    x = p[i-1]+p[i]
    x/=2
    #stma.insert(i,x)
    stma.append(x)
    temp= p[5-i]/5+temp
    #ltma.insert(i,temp)
    ltma.append(temp)

for i in range (len(stma)):
    if (stma[i-1]>ltma[i-1] and stma[i]<=ltma[i]) or (stma[i-1]<ltma[i-1] and stma[i]>=ltma[i]) or (stma[i-1]==ltma[i-1] and stma[i] != ltma[i]):
        print("{0} {1:.2f} {2:.2f}".format(i, stma[i], ltma[i]))
