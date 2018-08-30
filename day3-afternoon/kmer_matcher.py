#!/usr/bin/env python3

import sys
import fasta

target = open( sys.argv[1] )
query = open( sys.argv[2] )
k = int( sys.argv[3] )


kmers = {}

reader = fasta.FASTAReader( target )

for ident, sequence in reader:
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in kmers:
            kmers[kmer] = [[ident,i]]
        else:
            kmers[kmer].append([ident, i])

comp = fasta.FASTAReader( query )

for qident, qsequence in comp:
    for i in range( 0, len(qsequence) - k ):
        kmer = qsequence[i:i+k]
        if kmer in kmers:
            hits_list = kmers[kmer]
            for hit in hits_list:
                print(hit[0], hit[1], i, kmer)
 