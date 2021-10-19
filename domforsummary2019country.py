with open("domestic2019all1.csv", 'r') as t1:
    count=0
    dict1={}
    dict3={}
    dict4={}
    for lines in t1:
        count+=1
        #if count==2:
        #    for x in lines.split(","):
        #        dict1[x+"WT"]=0
        #        dict1[x+"Var"]=0
        #        dict1[x+"NA"]=0
        #if count==3:
        #    print(lines)
                
        if count>2:
            #print(lines)
            #break
            for x in range(1,len(lines.split(","))-2):
                #print(x)
                #print(lines.split(",")[x])
                #print(lines.split(",")[x])
                #if lines.split(",")[x]==" ":
                #    print("True")
                if lines.split(",")[x]!="":
                    #print(x)
                    #if x<len(lines.split(","))-2:
                    if lines.split(",")[x]=="WT":
                        if (x,"WT",lines.split(",")[64]) in dict3:
                            dict3[x,"WT",lines.split(",")[64]]=dict3[x,"WT",lines.split(",")[64]]+1
                    if "%" in lines.split(",")[x]:
                        if (x,"Var",lines.split(",")[64]) in dict3:
                            dict3[x,"Var",lines.split(",")[64]]=dict3[x,"Var",lines.split(",")[64]]+1
                    if lines.split(",")[x]=="None":
                        if (x,"None",lines.split(",")[64]) in dict3:
                            dict3[x,"None",lines.split(",")[64]]=dict3[x,"None",lines.split(",")[64]]+1
                    if lines.split(",")[x]=="WT":
                        if (x,"WT",lines.split(",")[64]) not in dict3:
                            dict3[x,"WT",lines.split(",")[64]]=1
                    if "%" in lines.split(",")[x]:
                        if (x,"Var",lines.split(",")[64]) not in dict3:
                            dict3[x,"Var",lines.split(",")[64]]=1
                    if lines.split(",")[x]=="None":
                        if (x,"None",lines.split(",")[64]) not in dict3:
                            dict3[x,"None",lines.split(",")[64]]=1
                    dict4[lines.split(",")[64]]=0
                    #print(x)
                    #print(lines.split(",")[x])
            #print(dict1)
            #break

#print(dict3)
#for item in dict3:
#    if "KE" in item:
#        print(dict3[item])
print(dict4)
with open("domestic2019all1summary2Country.csv", 'w') as t1:
    t1.write("Gene,wildtype,SNP,NA,Country\n")

with open("domestic2019all1.csv", 'r') as t1:
    with open("domestic2019all1summary2Country.csv", 'a') as t2:
        count=0
        dict2={}
        for lines in t1:
            count+=1
            if count==2:
                #print(lines)
                #linecount=0
                for x in range(1,len(lines.split(","))-2):
                    #print(x)
                    #break
                    total=0
                    #linecount+=1
                    #if linecount>1:
                        #print(lines)
                        #break
                        #print(x)
                        #print(linecount)
                        #if x=="":
                        #    print("True")
                    #if lines.split(",")[x]==" ":
                    #    print("true")
                    #print(lines.split(",")[64])
                    if lines.split(",")[x]!="":
                        #print(x)
                        for items in dict4:
                            #print(items[2])
                            #print(items)
                            temp=""
                            if (x,"WT",items) in dict3:
                                #print(lines.split(",")[64])
                                #print(lines.split(",")[x]+","+str(dict3[x,"WT",lines.split(",")[64]]))
                                temp=lines.split(",")[x]+","+str(dict3[x,"WT",items])
                                #print(temp)
                                #total+=dict1[x,"WT"]
                                #dict2[lines.split(",")[x],"WT"]=dict1[x,"WT"]
                            if (x,"WT",items) not in dict3:
                                #print(lines.split(",")[64])
                                #print(lines.split(",")[x]+","+str(dict3[x,"WT",lines.split(",")[64]]))
                                temp=lines.split(",")[x]+","
                                #print(temp)
                                #total+=dict1[x,"WT"]
                                #dict2[lines.split(",")[x],"WT"]=dict1[x,"WT"]
                            if (x,"Var",items) in dict3 and (x,"None",items) not in dict3:
                                #print("True")
                                temp+=","+str(dict3[x,"Var",items])+"\n"
                                #dict2[lines.split(",")[x],"Var"]=dict1[x,"Var"]
                            if (x,"Var",items) in dict3 and (x,"None",items) in dict3:
                                temp+=","+str(dict3[x,"Var",items])
                                #dict2[lines.split(",")[x],"Var"]=dict1[x,"Var"]
                                #total+=dict1[x,"Var"]
                            if (x,"Var",items) not in dict3:
                                temp+=","
                                #dict2[x,"Var"]=dict1[linecount,"Var"]
                                #total+=dict1[linecount,"Var"]    
                            if (x,"None",items) in dict3:
                                temp+=","+str(dict3[x,"None",items])+","+items+"\n"
                                #dict2[lines.split(",")[x],"NA"]=dict1[x,"NA"]
                                #total+=dict1[x,"NA"]
                            if (x,"None",items) not in dict3:
                                temp+=",,"+str(items)+"\n"
                                #dict2[lines.split(",")[x],"NA"]=dict1[x,"NA"]
                            print(temp)
                            t2.write(temp)
                    #if x!="":
                            #if total==213:
                            #    print(x)
    #with open("domestic2019allsummary1.csv", 'w') as t1:

    