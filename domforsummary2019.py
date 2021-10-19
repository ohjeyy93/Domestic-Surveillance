with open("domestic2019all1.csv", 'r') as t1:
    count=0
    dict1={}
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
                    #print(lines.split(",")[x])
                    #print(x)
                    if lines.split(",")[x]=="WT":
                        if (x,"WT") in dict1:
                            dict1[x,"WT"]=dict1[x,"WT"]+1
                    if "%" in lines.split(",")[x]:
                        if (x,"Var") in dict1:
                            dict1[x,"Var"]=dict1[x,"Var"]+1
                    if lines.split(",")[x]=="None":
                        if (x,"NA") in dict1:
                            dict1[x,"NA"]=dict1[x,"NA"]+1
                    if lines.split(",")[x]=="WT":
                        if (x,"WT") not in dict1:
                            dict1[x,"WT"]=1
                    if "%" in lines.split(",")[x]:
                        if (x,"Var") not in dict1:
                            dict1[x,"Var"]=1
                    if lines.split(",")[x]=="None":
                        if (x,"NA") not in dict1:
                            dict1[x,"NA"]=1
            #print(dict1)
            #break

#print(dict1)

with open("domestic2019all1summary.csv", 'w') as t1:
    t1.write("Gene,wildtype,SNP,NA\n")

with open("domestic2019all1.csv", 'r') as t1:
    with open("domestic2019all1summary.csv", 'a') as t2:
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

                    if lines.split(",")[x]!="":
                        #print(x)
                        temp=""
                        if (x,"WT") in dict1:
                            temp=lines.split(",")[x]+","+str(dict1[x,"WT"])
                            total+=dict1[x,"WT"]
                            dict2[lines.split(",")[x],"WT"]=dict1[x,"WT"]
                        if (x,"Var") in dict1 and (x,"NA") not in dict1:
                            temp+=","+str(dict1[lines.split(",")[x],"Var"])+"\n"
                            dict2[lines.split(",")[x],"Var"]=dict1[x,"Var"]
                        if (x,"Var") in dict1 and (x,"NA") in dict1:
                            temp+=","+str(dict1[x,"Var"])
                            dict2[lines.split(",")[x],"Var"]=dict1[x,"Var"]
                            total+=dict1[x,"Var"]
                        if (x,"Var") not in dict1:
                            temp+=","
                            #dict2[x,"Var"]=dict1[linecount,"Var"]
                            #total+=dict1[linecount,"Var"]    
                        if (x,"NA") in dict1:
                            temp+=","+str(dict1[x,"NA"])+"\n"
                            dict2[lines.split(",")[x],"NA"]=dict1[x,"NA"]
                            total+=dict1[x,"NA"]
                        t2.write(temp)
                    #if x!="":
                            #if total==213:
                            #    print(x)
    #with open("domestic2019allsummary1.csv", 'w') as t1:

    