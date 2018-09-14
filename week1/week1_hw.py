#!/usr/bin/env python3
""" Usage: ./week1_hw.py <aligned AA file> <DNA seq blast>"""
# compare aligned amino acid file to DNA sequence to replace DNA sequence with gaps where there are gaps in protein alignment

import sys
import fasta

prot = open( sys.argv[1] )
dna = open( sys.argv[2] )


prot_reader = fasta.FASTAReader(prot)
dna_reader = fasta.FASTAReader(dna)

for (prot_id, prot_seq), (dna_id, dna_seq) in zip(prot_reader, dna_reader):
    
    dna_mod = []
    count = 0
    for prot_aa in prot_seq:
        if prot_aa == "-":
            dna_mod.append("---")
        else:
            dna_mod.append(dna_seq[count:count + 3])
            count += 3
            
    print(dna_mod)

            

        