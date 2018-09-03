#!/usr/bin/env python3

"""
Usage: ./mark-regressv2.py <tab file1> <tab file2> <tab file3> <tab file4> <tab file5> <ctab file>

"""

import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf


#Define variables from each mark and ctab file
name1 = sys.argv[1].split(os.sep)[-1].split('.')[0]
tab1 = pd.read_csv(sys.argv[1], sep="\t").iloc[:, 4]

name2 = sys.argv[2].split(os.sep)[-1].split('.')[0]
tab2 = pd.read_csv(sys.argv[2], sep="\t").iloc[:, 4]

name3 = sys.argv[3].split(os.sep)[-1].split('.')[0]
tab3 = pd.read_csv(sys.argv[3], sep="\t").iloc[:, 4]

name4 = sys.argv[4].split(os.sep)[-1].split('.')[0]
tab4 = pd.read_csv(sys.argv[4], sep="\t").iloc[:, 4]

name5 = sys.argv[5].split(os.sep)[-1].split('.')[0]
tab5 = pd.read_csv(sys.argv[5], sep="\t").iloc[:, 4]

name6 = sys.argv[6].split(os.sep)[-2]
ctab_fpkms = pd.read_csv(sys.argv[6], sep="\t").iloc[:, -1]

#make dictionary and dataframe
mark_dict = {name1 : tab1, name2 : tab2, name3 : tab3, name4 : tab4, name5 : tab5, name6 : ctab_fpkms}
mark_df = pd.DataFrame(mark_dict)

#use statsmodels to generate regression model and print
mod = smf.ols(formula="{} ~ {} + {} + {} + {} + {}".format(name6, name1, name2, name3, name4, name5),data=mark_df)
res = mod.fit()
print(res.summary())
