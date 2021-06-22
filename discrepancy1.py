import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import re

sns.set_theme(style="white", context="talk")

df = pd.read_csv("testdomvaffix1.csv")
wholemutationcount=[]
wholewildtypecount=[]
wholemutcombo=[]
wholewildcombo=[]
with open("testdiscrepancy2.csv", "w") as t1:
    for x in range(len(df)):
        mutationcount=0
        wildtypecount=0
        tempmutcombo=[]
        tempwildcombo=[]
        #print(df.loc[1][3])
        #print(df.iloc[0,3])
        #print(df.columns[3])
        tempcount=3
        #print(df.columns)
        #print(len(df.loc[0]))
        #print(len(df.columns))
        tempnf=""
        tempnfmut=""
        tempgn=""
        tempgnmut=""
        tempcount=0
        for y in (df.loc[x][3::]):
            if type(y)==str:
                if any(map(str.isdigit, y)) or y=="Major" or y=="Minor":
                    if re.search('[a-zA-Z]', y):
                        tempcount+=1
                        if tempcount==2 and y=="Major" or y =="Minor":
                            tempnf="mutation"
                            tempnfmut=y
                        if tempcount==3 and any(map(str.isdigit, y)):
                            #print(y)
                            tempgn="mutation"
                            tempgnmut=y
                            #print(tempgnmut)
        if tempnf!=tempgn:
            #print(tempnfmut,tempgnmut)
            for k in range(len(df.loc[x])):
                if k<len(df.loc[x])-1:
                    t1.write(df.loc[x][k]+",")
                else:
                    t1.write(df.loc[x][k]+"\n")
                        