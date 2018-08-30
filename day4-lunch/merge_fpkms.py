#!/usr/bin/env python3

"""
Usage: ./merge_fpkms.sh <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen>
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#set threshold and dictionary
t = sys.argv[1]
fpkms = {}

for transcript in range( 2,len( sys.argv )):
    name = sys.argv[transcript].split( os.sep )[-2]
    fpkm = pd.read_csv( sys.argv[transcript], sep="\t", index_col="t_name" ).loc[:,"FPKM"]
    fpkms[name] = fpkm


fpkms_df = pd.DataFrame( fpkms )

fpkms_df["Sum"] = fpkms_df[list(fpkms_df)].sum(axis=1)


roi = fpkms_df.loc[:,"Sum"] > float(t)
fpkms_df.loc[roi, fpkms_df.columns != "Sum"].to_csv(sys.stdout, sep="\t") 


# fig, ( ax1, ax2 ) = plt.subplots(2)
# ax1.hist( gene_lengths )
# ax2.hist( gene_exons )
#
# fig.savefig("two_plots.png")
# plt.close( fig )