#!/usr/bin/env python3

"""
Usage:  ./week4plotpca.py plink.eigenvec
"""

import matplotlib
matplotlib.use("TkAgg")
import sys
import matplotlib.pyplot as plt
from statsmodels.stats import weightstats as stests
import numpy as np
import math


comp_1 = []
comp_2 = []

for line in open(sys.argv[1]):
	fields = line.rstrip("\r\n").split(" ")
	comp_1_x = fields[2]
	comp_2_y = fields[3]
	comp_1.append(float(comp_1_x))
	comp_2.append(float(comp_2_y))

fig, ax = plt.subplots()
plt.scatter(comp_1, comp_2)
plt.ylabel("relatedness")        
plt.xlabel("individual")   
ax.set_title("PCA")  
plt.tight_layout()    
#plt.xlim(0, 100000)
#plt.ylim(0, 120000)
fig.savefig("PCA.png")
plt.close(fig)