#!/usr/bin/env python3

import sys
f = open( sys.argv[1])

count = 0
for line in f :
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split()
    if fields[2] == "gene" and fields[17] == "\"protein_coding\";":
        count += 1
print(count)
        