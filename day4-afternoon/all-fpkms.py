#!/usr/bin/env python3

"""
Usage: ./all-fpkms.py <csv file> <data file>
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv( sys.argv[1] )

fpkms = {}

for index, sample, sex, stage in df.itertuples():
    filename = os.path.join( sys.argv[2], sample, "t_data.ctab" )
    ctab = pd.read_table( filename, index_col="t_name" ).loc[:,"FPKM"]
    header = str(sex + "_" + stage)
    fpkms[header] = ctab


ctab_all = pd.DataFrame(fpkms)
      
print(ctab_all)

