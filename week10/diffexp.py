#!/usr/bin/env python3

"""
Usage: ./diffexp.py <data file>
"""
#week10 differentially expressed genes from microarray data

import matplotlib
matplotlib.use("TkAgg")
import sys
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import scipy.cluster.vq as vac
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import ttest_ind


data1 = open(sys.argv[1])

#create dataframe
dataFrame = pd.read_table(data1, sep="\t", header = 0, index_col =0)
array = dataFrame.values


transposed_array = np.transpose(array)
transposed_dataframe = dataFrame.transpose()


Z = linkage(transposed_array,'ward')


cell_name= leaves_list(Z)
cell_names_ordered = transposed_dataframe.index.values[cell_name]

#differentially expressed genes

early = ["CFU", "mys"]
late = ["poly", "unk"]

t_stat, p_val = ttest_ind(dataFrame[early], dataFrame[late], axis = 1)
dataFrame["p_value"] = p_val

dataFrame = dataFrame.mask(dataFrame["p_value"] > 0.05).dropna(how = "any").sort_values ("p_value")


#print (on screen or send to file) list of differentially expressed genes
print(dataFrame.ix[:,4].to_csv(sep='\t'))
