#!/usr/bin/env python3

import sys


if len(sys.argv) > 1:
    f = open( sys.argv[1] )
else: 
    f = sys.stdin
 
count = 0
total = 0

for i, line in enumerate( f ):
    if line[0] == "@":
        continue
    cut = line.strip().split("\t")
    count += 1
    total += int(cut[4])
    
        
average = total / count

print(average)