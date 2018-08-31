#!/usr/bin/env python3

"""
Ordinary linear regression on five tab files using OLS
"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import os


#df = pd.read_tab( sys.argv[])

#for i in 

name1 = sys.argv[1].split( os.sep )[-1].split('.')[0]
tab1 = pd.read_csv( sys.argv[1], sep="\t" ).iloc[:, 4]
name2 = sys.argv[2].split( os.sep )[-1].split('.')[0]
tab2 = pd.read_csv( sys.argv[2], sep="\t" ).iloc[:, 4]
name3 = sys.argv[3].split( os.sep )[-1].split('.')[0]
tab3 = pd.read_csv( sys.argv[3], sep="\t" ).iloc[:, 4]
name4 = sys.argv[4].split( os.sep )[-1].split('.')[0]
tab4 = pd.read_csv( sys.argv[4], sep="\t" ).iloc[:, 4]
name5 = sys.argv[5].split( os.sep )[-1].split('.')[0]
tab5 = pd.read_csv( sys.argv[5], sep="\t" ).iloc[:, 4]
name6 = sys.argv[6].split( os.sep )[-2]
tab6 = pd.read_csv( sys.argv[6], sep="\t" ).iloc[:, -1]

mean0_dict = {name1 : tab1, name2 : tab2, name3 : tab3, name4 : tab4, name5 : tab5, name6 : tab6}
means_df = pd.DataFrame( mean0_dict  )


#print(means_df)
mod = smf.ols(formula="SRR072893 ~ {} + {} +{} +{} +{}".format(name1, name2, name3, name4, name5), data=means_df)
res = mod.fit()

print(res.summary())