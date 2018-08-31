#!/usr/bin/env python3

"""
Usage: ./hwtc.py <t_name> <samples.csv> <ctab_dir> <replicates>

Create a timecourse of a given transcript (FBtr0331261)
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt



def timecourse(gender):
    df = pd.read_csv( sys.argv[2] )
    soi = df.loc[:, "sex"] == str(gender) 
    df = df.loc[soi,:]

    fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[3], sample, "t_data.ctab" )
        ctab_df = pd.read_table( filename, index_col="t_name" )
        fpkms.append( ctab_df.loc[sys.argv[1],"FPKM"] )
    return fpkms

male_fpkms = timecourse("male")
female_fpkms = timecourse("female")

def timecourse_rep(gender):
    df = pd.read_csv( sys.argv[4] )
    soi = df.loc[:, "sex"] == str(gender) 
    df = df.loc[soi,:]

    fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[3], sample, "t_data.ctab" )
        ctab_df = pd.read_table( filename, index_col = "t_name" )
        fpkms.append( ctab_df.loc[sys.argv[1],"FPKM"] )
    return fpkms

rep_male_fpkms = timecourse_rep("male")
rep_female_fpkms = timecourse_rep("female")

my_x = ("9","10","11","12","13","14a","14b","14c","14d")

    
fig, ax = plt.subplots()
ax.plot( male_fpkms, c = "blue" )
ax.plot( female_fpkms, c = "red" )
ax.plot([4,5,6,7], rep_male_fpkms, c = "green")
ax.plot([4,5,6,7], rep_female_fpkms, c = "orange")
ax.set_title("FBtr", style= 'italic')
ax.set_xlabel("developmental stage")
ax.set_ylabel("mRNA abundance FPKMs")
ax.set_xticklabels(labels = my_x)
plt.xticks(rotation=90)
plt.legend(["male", "female", "male reps", "female reps"], loc = 'center left', bbox_to_anchor = (1,0.5))
plt.tight_layout()
fig.savefig( "d4hwtcr.png" )
plt.close()
