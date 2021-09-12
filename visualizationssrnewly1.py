import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import re

sns.set_theme(style="white", context="talk")

df = pd.read_csv("testdomsamfixbp22.csv")
wholemutationcount=[]
wholewildtypecount=[]
wholemutcombo=[]
wholewildcombo=[]
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
    if df.loc[x][1]!="basepos" and df.loc[x][1]!="coverage" and df.loc[x][1]!="Variant frequency":
        for y in (df.loc[x][3::]):
            if type(y)==str:
                if re.search('[a-zA-Z]', y):
                    #print(y)
                    #print(y)
                    mutationcount+=1
                    tempmutcombo+=[df.columns[tempcount]]
            tempcount+=1
            #print(y)
        if mutationcount!=0:
            wholemutationcount+=[mutationcount]
            wholemutcombo+=[tempmutcombo]

#print(wholemutationcount)
#print(wholemutcombo)


#print(wholemutationcount)
#print(wholewildtypecount)

dict1={}
#print(wholewildcombo)
#print(wholemutcombo)
#print(len(wholemutationcount))
for x in range(len(wholemutationcount)):
    if str(wholemutcombo[x]) not in dict1:
        dict1[str(wholemutcombo[x])]=1
    if str(wholemutcombo[x]) in dict1:
        dict1[str(wholemutcombo[x])]+=1
for x in range(len(wholewildtypecount)):
    if str(wholewildcombo[x]) not in dict1:
        dict1[str(wholewildcombo[x])]=1
    if str(wholewildcombo[x]) in dict1:
        dict1[str(wholewildcombo[x])]+=1

#print(len(dict1))
# Generate some sequential data
x = np.array(list("ABCDEFGHIJKLM"))
x1=[]
y1=[]
for items in dict1:
    x1+=[items]
    y1+=[dict1[items]]
gs = gridspec.GridSpec(2,2)
axs1=plt.subplot(gs[0,1])
y=y1
#print(y1)
my_cmap = plt.get_cmap("viridis")
#rescale = lambda y: (y - np.min(y)) / (np.max(y) - np.min(y))*3
#print(len(x))
NUM_COLORS=13
cm = plt.get_cmap('gist_rainbow')
axs1.bar(x,y1, width=0.3, color=[cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])
axs1.xaxis.set_major_formatter(plt.NullFormatter())
axs1.set_ylabel('Vairant call overlaps')
#sns.barplot(x=x, y=y1, palette="rocket")
axs2=plt.subplot(gs[1,1])
y2=[]
for x in range(3,len(df.columns)):
    y2+=[df.columns[x]]

wholelist1=[]
for items in dict1:
    templist1=[]
    for y in (items.split(",")):
        for x in range(3,len(df.columns)):
            #print(y.strip("[").strip("]"))
            #print(df.columns[x])
            if df.columns[x] in y.strip("[").strip("]"):
                templist1+=[x-2]
    wholelist1+=[templist1]

#print(wholelist1)
#plt.scatter(x=[1,2,3,4,5,6,7,8,9],y=y2)
#plt.scatter(x=[1],y=[(1,2,3,4,5)])
XVals = np.array(list("ABCDEFGHIJKLM"))
YVals = wholelist1

X = [XVals[i] for i, data in enumerate(YVals) for j in range(len(data))]
Y = [val for data in YVals for val in data]

axs2.scatter(X, Y, s=100)
#print(X,Y)
tempx=""
templistx=[]
templisty=[]
for x in range(len(X)):
    if tempx=="":
        tempx=X[x]
        templistx+=[X[x]]
        templisty+=[Y[x]]
    if tempx==X[x]:
        tempx=X[x]
        templistx+=[X[x]]
        templisty+=[Y[x]]
    if tempx!=X[x]:
        axs2.plot(templistx,templisty, color="blue")
        tempx=X[x]
        templistx=[]
        templisty=[]
        templistx+=[X[x]]
        templisty+=[Y[x]]
axs2.plot(templistx,templisty, color="blue")
axs2.xaxis.set_major_formatter(plt.NullFormatter())
#print(X)
#fig, ax = plt.subplots()
#ax.set_yticks([1,2,3,4,5,7,8,9])
#ax.set_yticks(y2)
#print(len(y2))
plt.yticks(np.arange(1,6),y2, fontsize=7)
axs3=plt.subplot(gs[1,0])
axs3.yaxis.set_major_formatter(plt.NullFormatter())


tempsum=[]
wholesum=[]
for y in range(3,len(df.loc[0])):
    tempsum=0
    for x in range(len(df)):
        if type(df.loc[x][y])==str:
            if re.search('[a-zA-Z]', df.loc[x][y]):
                tempsum+=1
    wholesum+=[tempsum]
count=0
maxnum=0
for y in (wholesum):
    count+=1
    axs3.hlines(count,xmin=0, xmax=y, color="green")

#print(wholesum)
maxnum=max(wholesum)
xticks=[]
for x in range(6):
    xticks+=[x*0.2*maxnum]

axs3.set_xlabel('Total number of variant calls')
#axs3.set_xticklabels(xticks)
axs3.invert_xaxis()
plt.subplots_adjust(hspace=0.01)
plt.show()
#for item in dict1:
#    print(item)
#print(len(dict1))
#print(dict1)
#print(dict1) 
    #print(df.loc[x])
    #print(wildtypecount)
    #print(mutationcount)
    #print(any(map(str.isdigit, df.iloc[x,3]))) 
    #print(any(map(str.isdigit, df.iloc[x,4]))) 
    #print(any(map(str.isdigit, df.iloc[x,5])))
    #print(any(map(str.isdigit, df.iloc[x,10])))
    #print(df.iloc[x,3],df.iloc[x,4],df.iloc[x,5],df.iloc[x,6],df.iloc[x,7],df.iloc[x,8],df.iloc[x,9],df.iloc[x,10],df.iloc[x,11])

#for x in wholemutcombo:
    #print(x)