#!/usr/bin/env python3

"""
Usage: ./all_freq.py <vsf file>"""

import matplotlib
matplotlib.use("TkAgg")
import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests
import numpy as np
import math

all_freq = []

for line in open(sys.argv[1]):
	if line.startswith("#"):
		continue
	else:
		fields = line.rstrip("\r\n").split("\t")
		frequency = fields[7]
		allele = frequency.split("=")[1]
		allele_2 = allele.split(",")[0]
		all_freq.append(float(allele_2))

fig, ax = plt.subplots()
plt.hist(all_freq)
plt.ylabel("frequency")        
plt.xlabel("allele")   
ax.set_title("allele frequency spectrum")  
plt.tight_layout()
fig.savefig("all_freq.png")
plt.close(fig)