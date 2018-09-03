#!/usr/bin/env python3

"""
Usage: ./approx-promoter.py <ctab file> <output bed file>
"""

import sys

f = open(sys.argv[1])

# skip header then iterate through each identifying + vs. - strands
# Convert string entries to integers and add/subtract to define promoter region
for line in f:
    if line.startswith("t_id"):
        continue
    fields = line.rstrip("/r/n").split()
    strand = fields[2]
    chromosome = fields[1]
    start = int(fields[3])
    end = int(fields[4])
    t_name = fields[5]    
    if strand == "+":
        p_start = start - 500
        p_end = start + 500
    if strand == "-":
        p_start = end + 500
        p_end = end - 500

#print statement for each transcript after promoter definition

    print(str(chromosome) + "\t" + str(p_start) + "\t" + str(p_end) + "\t" + t_name)
     
         