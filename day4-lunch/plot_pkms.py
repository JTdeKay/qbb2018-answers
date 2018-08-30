#!/usr/bin/env python3

"""
Usage: ./merge_fpkms.sh <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

t = sys.argv[1]

name1 = sys.argv[1].split( os.sep )[-2]
fpkm1 = pd.read_csv( sys.argv[1], sep="\t", index_col="t_name" ).loc[:,"FPKM"]
#logfpkm1 = np.log(fpkm1+1)

name2 = sys.argv[2].split( os.sep )[-2]
fpkm2 = pd.read_csv( sys.argv[2], sep="\t", index_col="t_name" ).loc[:,"FPKM"]



coeff = np.polyfit(fpkm1,fpkm2,1) 
polynomial = np.poly1d(coeff)
x = np.linspace(0, 10000)


fig, ax= plt.subplots()
ax.scatter(fpkm1, fpkm2, alpha = 0.2, s = 3)
fig.suptitle("FPKM Comparison")
ax.set_xlabel("FPKM1")
ax.set_ylabel("FPKM2")
ax.set_xscale('log')
ax.set_yscale('log')

plt.plot(x, polynomial(x), 'k')
plt.text(7,5,str(polynomial))
plt.axis([0.001, 10000, 0.001, 10000])
fig.savefig("compare.png")
plt.close( fig )





