#!/usr/bin/env python3

"""
Usage: ./merge_fpkms.py <threshold> <ctab_file1> <ctab_file2> ... <ctab_filen>

Combine FPKM values from 2 or more ctab files specifying a threshold for total FPKM.
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

#set dataframe
fpkms_df = pd.DataFrame( fpkms )

fpkms_df["Sum"] = fpkms_df[list(fpkms_df)].sum(axis=1)

#define row of interest
roi = fpkms_df.loc[:,"Sum"] > float(t)
fpkms_df.loc[roi, fpkms_df.columns != "Sum"].to_csv(sys.stdout, sep="\t") 


