#!/usr/bin/env python3


import sys

f = open(sys.argv[1])

for i in f:
    i = i.strip("\n")
    i = i.split("\t")
    print(">" + i[0])
    print(i[1])
    
    
    
    