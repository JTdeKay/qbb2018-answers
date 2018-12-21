#!/usr/bin/env python3

""" Usage: ./week6hw.py peaksgained peakslost Mm_features.bed """

import matplotlib
matplotlib.use("TkAgg")
import sys
import matplotlib.pyplot as plt
import numpy as np

CTCFgain = open(sys.argv[1])
CTCFloss = open(sys.argv[2])
Mmf = open(sys.argv[3])

GDict = {}
LDict = {}
for line in Mmf:
    fieldsF=line.rstrip("\r\n").split("\t")
    CTCFgain.seek(0)
    CTCFloss.seek(0)
    for i, line in enumerate (CTCFgain):
        fieldsG=line.rstrip("\r\n").split("\t")
        if ((int(fieldsG[1]) <= int(fieldsF[2])) & (int(fieldsG[1]) >= int(fieldsF[1]))) | (((int(fieldsG[2]) <= int(fieldsF[2])) & int(fieldsG[2]) >= int(fieldsF[1]))):
            if (fieldsF[3]) in GDict:
                GDict[fieldsF[3]] += 1
            else:
                GDict[fieldsF[3]] = 1
    for j, line in enumerate (CTCFloss):
        fieldsL=line.rstrip("\r\n").split("\t")
        if ((int(fieldsL[1]) <= int(fieldsF[2])) & (int(fieldsL[1]) >= int(fieldsF[1]))) | (((int(fieldsL[2]) <= int(fieldsF[2])) & int(fieldsL[2]) >= int(fieldsF[1]))):           
            if (fieldsF[3]) in LDict:
                LDict[fieldsF[3]] += 1
            else:
                LDict[fieldsF[3]] = 1

otherg = numGain = i+1
otherl = numLoss = j+1
for value in GDict:
    otherg = otherg - GDict[value]
for value in LDict: 
    otherl = otherl - LDict[value]
GDict['other'] = otherg
LDict['other'] = otherl
LtX = []
LtY = []
for key in GDict:
    LtX.append("Gain in " + key)
    LtY.append(GDict[key])
for key in LDict: 
    LtX.append("Loss in " + key)
    LtY.append(LDict[key])
    
fig, axes = plt.subplots(1,2)
fig.suptitle(" ")
axes[0].set_xlabel("Site")
axes[0].set_ylabel("Number")
axes[0].bar(LtX, LtY, color=['blue', 'blue', 'blue', 'blue', 'green', 'green', 'green', 'green'])
axes[0].tick_params('x', rotation=20)
axes[1].set_xlabel("Site")
axes[1].set_ylabel("Number")
axes[1].bar(['Gained', 'Lost'], [numGain, numLoss], color=['blue','green'])
fig.savefig("wk6fig.png")
plt.close(fig)


        
                
