#!/usr/bin/env python3


import sys
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets




df = pd.read_table(sys.argv[1], sep = "\t", header=0, index_col=0)

matrix = df.values
#print(df)
#print(matrix)

Z = linkage(matrix.T, "ward")

fig, ax = plt.subplots()
plt.title("Dendrogram")
plt.xlabel("sample")
plt.ylabel("distance")
dendrogram(
    Z,
    show_leaf_counts=False,
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True)

fig.savefig("dendrogram.png")
plt.close(fig)



