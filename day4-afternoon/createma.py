#!/usr/bin/env python3

"""
Create MA plot
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


name1 = sys.argv[1].split( os.sep )[-2]
fpkm1 = pd.read_csv( sys.argv[1], sep="\t", index_col="t_name" ).loc[:,"FPKM"]

name2 = sys.argv[2].split( os.sep )[-2]
fpkm2 = pd.read_csv( sys.argv[2], sep="\t", index_col="t_name" ).loc[:,"FPKM"]


m = np.log2((fpkm1+1)/(fpkm2+1))
a = np.log2((fpkm1+1)*(fpkm2+1))*0.5


fig, ax= plt.subplots()
ax.scatter(a, m, alpha = 0.2, s = 3)
fig.suptitle("MA plot")
ax.set_xlabel("Mean Expression Level")
ax.set_ylabel("Log Fold Change")

plt.axis([0, 12, -8, 8])
fig.savefig("ma_plot.png")
plt.close( fig )



