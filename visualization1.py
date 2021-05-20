import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="white", context="talk")

df = pd.read_csv("testnew3.csv")
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
    for y in (df.loc[x][3::]):
        #print(y)
        if y=="WT" or y=="Wildtype":
            wildtypecount+=1
            tempwildcombo+=[df.columns[tempcount]]
        if type(y)==str:
            if any(map(str.isdigit, y)) or y=="Major" or y=="Minor":
                mutationcount+=1
                tempmutcombo+=[df.columns[tempcount]]
        tempcount+=1
        #print(y)
    if mutationcount!=0:
        wholemutationcount+=[mutationcount]
        wholemutcombo+=[tempmutcombo]
    if wildtypecount!=0:
        wholewildtypecount+=[wildtypecount]
        wholewildcombo+=[tempwildcombo]

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
x = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZa"))
x1=[]
y1=[]
for items in dict1:
    x1+=[items]
    y1+=[dict1[items]]
plt.subplot(2,1,1)
sns.barplot(x=x, y=y1, palette="rocket")
plt.subplot(2, 1, 2)
y2=[]
for x in range(3,len(df.columns)):
    y2+=[df.columns[x]]

wholelist1=[]
for items in dict1:
    templist1=[]
    for y in (items.split(",")):
        for x in range(3,len(df.columns)):
            print(y.strip("[").strip("]"))
            print(df.columns[x])
            if df.columns[x] in y.strip("[").strip("]"):
                templist1+=[x-2]
    wholelist1+=[templist1]

print(wholelist1)
#plt.scatter(x=[1,2,3,4,5,6,7,8,9],y=y2)
#plt.scatter(x=[1],y=[(1,2,3,4,5)])
XVals = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZa"))
YVals = wholelist1

X = [XVals[i] for i, data in enumerate(YVals) for j in range(len(data))]
Y = [val for data in YVals for val in data]

plt.scatter(X, Y, s=100)

#fig, ax = plt.subplots()
#ax.set_yticks([1,2,3,4,5,7,8,9])
#ax.set_yticks(y2)
plt.yticks(np.arange(1,10),y2)
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