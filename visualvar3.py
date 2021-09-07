import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import re

sns.set_theme(style="white", context="talk")

df = pd.read_csv("testdomsamfixbp21.csv")
nfnestnumvar1=0
geneiousnumvar1=0
disagree1=0
agree1=0
previousdisagree=0
flag=""
for x in range(len(df)):
    #for y in (df.loc[x][1]):
    flag="normal"
    nf1=""
    gn1=""
    if type(df.loc[x][3])!=float:
        if df.loc[x][1]!="basepos" and df.loc[x][1]!="coverage" and df.loc[x][1]!="Variant frequency":
            if any(map(str.isdigit, df.loc[x][3])):
                #print(df.loc[x][3])
                nfnestnumvar1+=1
                nf1=df.loc[x][3]
    if type(df.loc[x][4])!=float:
        if df.loc[x][1]!="basepos" and df.loc[x][1]!="coverage" and df.loc[x][1]!="Variant frequency":
            if any(map(str.isdigit, df.loc[x][4])):
                #print(df.loc[x][4])
                geneiousnumvar1+=1
                gn1=df.loc[x][4]
    if nf1!="" or gn1!="":
        if nf1==gn1:
            agree1+=1
        else:
            #if gn1!="":
            #    print(df.loc[x])
            disagree1+=1
                #if df.loc[x][3]!=df.loc[x][4]:
                #    if previousdisagree==disagree1:
                #        disagree1+=1

        #print(df.loc[x][3])
        #print(df.loc[x][4])

listcov1=[nfnestnumvar1,geneiousnumvar1,agree1]
listrange1=["nfnestvar","geneiousvar","agree"]

print(listcov1)

NUM_COLORS=3
gs = gridspec.GridSpec(2,2)
cm = plt.get_cmap('gist_rainbow')
axs1=plt.subplot(gs[0,1])
axs1.bar(listrange1,listcov1, width=0.3, color=[cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
axs1.xaxis.set_major_formatter(plt.NullFormatter())
axs1.set_ylabel('Number of variants identified')
axs1.set_xticklabels(listrange1, fontsize=13)

plt.subplots_adjust(hspace=0.1, wspace=0.5)
plt.show()