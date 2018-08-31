#!/usr/bin/env python3

"""
Usage: ./d4q3.py 

Arbitrary number of gene names to plot
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


def general_gend(gender, gene):
    df = pd.read_csv(sys.argv[1])
    soi = df.loc[:,"sex"] == gender
    df = df.loc[soi,:]
    

    all_fpkms = []
    mean_fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[2], sample, "t_data.ctab" )
        ctab_df = pd.read_table( filename, index_col="t_name" )
        roi = ctab_df.loc[:,"gene_name"] == gene
        all_fpkms.append(ctab_df.loc[roi, "FPKM"])
        mean_fpkms.append(np.mean(all_fpkms))
    return mean_fpkms


for name in sys.argv[4: len(sys.argv)]:
    mean_m_fpkms = general_gend( "male", name)
    mean_f_fpkms = general_gend("female", name)


fig, ax = plt.subplots()
ax.plot( mean_m_fpkms, c = "blue" )
ax.plot( mean_f_fpkms, c = "red" )
ax.set_title(str(name), style= 'italic')
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance")

my_x = ["9", "10", "11", "12", "13", "14a", "14b", "14c", "14d"]
ax.set_xticklabels(labels = my_x)
plt.xticks(rotation=90)
plt.legend(["male", "female"], loc = 'center left', bbox_to_anchor = (1,0.5))
plt.tight_layout()
fig.savefig("mean_trans_timec_" + str(name) + ".png")
plt.close()
