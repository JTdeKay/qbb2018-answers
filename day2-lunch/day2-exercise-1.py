#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open( sys.argv[1] )
else: 
    f = sys.stdin
 
count =0    
for i, line in enumerate( f ):
    if line[0] == "@":
        continue
    count += 1


print(count)
  #      if count >10:
  #          break    
        
#    fields = line.rstrip("\r\n").split("\t")
 #   tx_len = int(fields[4]) - int(fields[3])
#    if tx_len > 10000:
#        print( fields[5], tx_len )
    