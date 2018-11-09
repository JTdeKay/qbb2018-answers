#!/usr/bin/env python3


import sys
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets




df = pd.read_table(sys.argv[1], header=0, index_col=0)

types = df.columns.values.tolist()
genes = df.index.tolist()

matrix = df.values
#print(df)
#print(matrix)

Z = linkage(matrix, "ward")
ZT = linkage(matrix.T, "ward")

fig, ax = plt.subplots()
plt.title("Dendrogram")
plt.xlabel("sample")
plt.ylabel("distance")
dendrogram(
    ZT,
    show_leaf_counts=False,
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True)

fig.savefig("dendrogram.png")
plt.close(fig)


idx_rows = leaves_list(Z)
data = matrix[idx_rows, :]
idx_columns = leaves_list(ZT)
data = data[:, idx_columns]

X = (data-np.average(data,axis=0))/np.std(data,axis=0)

m = np.max(np.abs(X))
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Heatmap by Cell Type")
im = ax.pcolor(
    X,
    cmap="RdBu",
    vmin=-1*m,
    vmax=m,
    )

ax.grid(False)
ax.set_xticks(
    np.arange(0.5, X.shape[1]+0.5),
    )
ax.set_xticklabels(
    idx_columns,
    rotation=50,
    )
ax.set_yticks([])

cbar = fig.colorbar(im, ax=ax)
fig.subplots_adjust(
    left = 0.05,
    bottom = 0.15,
    right = 1.0,
    top = 0.95
)

fig.savefig("heatmap.png")
plt.close(fig)
