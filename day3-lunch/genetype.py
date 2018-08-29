#!/usr/bin/env python3

import sys

flydata = {}
f = open( sys.argv[1])

for line in f :
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split()
    if fields[2] == "gene":
        biotype = fields[17]
        if biotype not in flydata:
            flydata[biotype] = 1
        else:
            flydata[biotype] += 1
        
print(flydata)       
        
        
