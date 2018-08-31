#!/usr/bin/env python3

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

f = open(sys.argv[1])

my_dict = {}

for line in f:
    if line.startswith("t_id"):
        continue
    fields = line.rstrip("/r/n").split()
    strand = fields[2]
    chromosome = fields[1]
    start = int(fields[3])
    end = int(fields[4])
    t_name = fields[5]    
    if strand == "+":
        p_start = start - 500
        p_end = start + 500
    if strand == "-":
        p_start = end + 500
        p_end = end - 500

    print(str(chromosome) + "\t" + str(start) + "\t" + str(end) + "\t" + t_name)

        

# for index, row in df.intertuples():
#     df = pd.read_csv(sys.argv[1], sep="\t")
#     if "strand" == "+":
#         start = row.loc[:, "strand"]
#         p_start = int(start) -500
#         df.loc[index, "start"] = p_end
#         end = row.loc[, "strand"]
#     start = int("start") -500

#
# coi = ctab_df.loc[:, ""]
     
         