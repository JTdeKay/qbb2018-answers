#!/usr/bin/env python3
"""This is for non-protein coding gene proximity"""

import sys

f = open( sys.argv[1])

find_pos = 21378950
short_dis = 10**9
close_gene = "NOPE"

for line in f :
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split()
    if fields[0] == "3R" and fields[2] == "gene" and fields[17] != "\"protein_coding\";":
        my_dist = 0
        if find_pos < int(fields[3]):
            my_dist = int(fields[3]) - find_pos
        elif find_pos > int(fields[4]):
            my_dist = find_pos - int(fields[4])
        if short_dis > my_dist:
            short_dis = my_dist    
            close_gene = fields[13]

print(close_gene, short_dis)
            

    # if fields[0] == "3R" and fields[2] == "gene" and fields[17] != "\"protein_coding\";":
    #     my_dist = 0
    #     if find_pos < fields[3]:
    #         my_dist = fields[3] - find_pos
    #     elif find_pos > fields[4]:
    #         my_dist = find_pos - fields[4]