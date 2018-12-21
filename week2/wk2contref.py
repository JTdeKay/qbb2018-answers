#!/usr/bin/env python3


"""
Usage: wk2contref.py <lastz.out> 
"""

import matplotlib
matplotlib.use("TkAgg")
import fasta
import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests
import numpy as np
import math

pos = 0
fig, ax = plt.subplots()
for i in open(sys.argv[1]):
	field = i.split("\t")
	ref_start = field[0]
	ref_end = field[1]
	contig_name = field[2]
	contig_strand = field[3]
	contig_start = field[4]
	contig_end = field[5]
	contig_len = field[6]
	plt.plot([int(ref_start), int(ref_end)], [pos, pos + int(contig_len)])
	pos += int(contig_len)


plt.ylabel("Contigs")        
plt.xlabel("Reference")   
ax.set_title("Contig position >= reference seq")  
plt.tight_layout()    
plt.xlim(0, 100000)
plt.ylim(0, 120000)
fig.savefig("dotplt1.png")
plt.close(fig)