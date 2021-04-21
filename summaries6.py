import os

wholefiles=[]
for subdir, dirs, files in os.walk("Allreports2"):
    for file in files:
        if "cali" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]
        if "cali" in subdir:
            if "known_variants.csv" in file:
                wholefiles+=[os.path.join(subdir, file)]

wholelist1=[]
dict1={}
with open("testnew.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
            #print(files)
            for lines in f1:
                count=0
                tempdict1=""
                tempgene1=""
                tempgene2=""
                #print(lines)
                for word in lines.split(","):
                    if (count==3 and "mycali" in files) or (count==3 and "caliReports" in files):
                        #print(word)
                        #print(lines)
                        tempdict1+=","
                        if word == "PfDHFR":
                            tempdict1+="DHFR"
                        if word == "PfDHPS":
                            tempdict1+="DHPS"
                        if word == "PfK13":
                            tempdict1+="K13"
                        if word in ["PfCRT","PfMDR1","CYTOb"]:
                            tempdict1+=word
                        #print(tempdict1)
                        #print(tempdict1)
                    if (count==4 and "mycali" in files) or (count==4 and "caliReports" in files):
                        #print(word)
                        #print(lines)
                        tempdict1+=","
                        tempdict1+=word
                    if count==5:
                        if word=="AAref":
                            tempdict1=""
                            break
                    if count==5 and "mycali" not in files and "caliReports" not in files:
                        tempdict1+=(","+word)
                    if count==6 and "mycali" not in files and "caliReports" not in files:
                        tempgene=word
                    if count==7 and "mycali" not in files and "caliReports" not in files:
                        tempdict1+=word
                        tempdict1+=tempgene
                        #print(lines)
                        #print(tempdict1)
                    if count==0:
                        if word=="Sample":
                            break
                        if "mycali" in files or "caliReports" in files:
                            if word.find("_")!=-1 and "mitochondrial" not in word:
                                tempdict1=word[0:word.find("_")]
                                #print(tempdict1)
                        if "mycali" not in files and "caliReports" not in files:
                            tempdict1=files[files.find("/")+1:files.find("_")]
                            #print(tempdict1)
                    if count==0 and "mycali" not in files and "caliReports" not in files:
                        tempdict1+=","
                        if word=="mitochondrial_genome":
                            tempdict1+="CYTOb"
                        else:tempdict1+=word
                    count+=1
                tempcount=0
                #print(tempdict1[0:2])
                if wholelist1==[] and tempdict1!='':
                    wholelist1+=[tempdict1]
                if tempdict1!="":
                    for item in wholelist1:
                        tempcount+=1
                        if tempdict1[0:2] == item[0:2] and tempdict1[-4:] == item[-4:]:
                            break
                        if tempcount==len(wholelist1):
                            wholelist1+=[tempdict1]
#print(wholelist1)

with open("testnew.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
            for lines in f1:
                count=0
                tempdict2=""
                tempgene1=""
                for word in lines.split(","):
                    if count==0 and "caliReports" in files:
                        #print(word)
                        if word=="Sample":
                            break
                        if word.find("_")!=-1 and "mitochondrial" not in word:
                            tempdict2=word[0:word.find("_")]
                                #print(tempdict1)
                            #print(tempdict1)
                    if (count==3 and "caliReports" in files):
                        #print(word)
                        #print(lines)
                        tempdict2+=","
                        if word == "PfDHFR":
                            tempdict2+="DHFR"
                        if word == "PfDHPS":
                            tempdict2+="DHPS"
                        if word == "PfK13":
                            tempdict2+="K13"
                        if word in ["PfCRT","PfMDR1","CYTOb"]:
                            tempdict2+=word
                    if (count==4 and "caliReports" in files):
                        #print(word)
                        #print(lines)
                        tempdict2+=","
                        tempdict2+=word
                        #print(tempdict1)
                        #print(tempdict1)
                        #print(tempdict2)
                    if count==5 and "caliReports" in files:
                        #print(word)
                        tempgene1=word
                    count+=1
                #print(tempgene1)
                tempcount=0
                if tempgene1!="":
                    for item in wholelist1:
                        tempcount+=1
                        if tempdict2[0:2] == item[0:2] and tempdict2[-4:] == item[-4:]:
                            #print(tempgene1)
                            if item not in dict1:
                                #print("True")
                                #print(tempgene1)
                                #print(tempgene1)
                                dict1[item]=","+tempgene1
                                break
for item in wholelist1:
    if item not in dict1:
        dict1[item]=",NA" 

#print(dict1)
#print(len(wholelist1))
#print((dict1))
#for item in wholelist1:
#    if item not in dict1:
#        print("False")
#print(len(dict1))
#print(dict1)

with open("testnew.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
            for lines in f1:
                count=0
                tempdict3=""
                tempgene1=""
                for word in lines.split(","):
                    if count==0 and "mycali" in files:
                        if word=="Sample":
                            break
                        if word.find("_")!=-1 and "mitochondrial" not in word:
                            tempdict3=word[0:word.find("_")]
                                #print(tempdict1)
                            #print(tempdict1)
                    if (count==3 and "mycali" in files):
                        #print(word)
                        #print(lines)
                        tempdict3+=","
                        if word == "PfDHFR":
                            tempdict3+="DHFR"
                        if word == "PfDHPS":
                            tempdict3+="DHPS"
                        if word == "PfK13":
                            tempdict3+="K13"
                        if word in ["PfCRT","PfMDR1","CYTOb"]:
                            tempdict3+=word
                    if (count==4 and "mycali" in files):
                        #print(word)
                        #print(lines)
                        tempdict3+=","
                        tempdict3+=word
                        #print(tempdict1)
                        #print(tempdict1)
                    if count==5 and "mycali" in files:
                        tempgene1=word
                    count+=1
                tempcount1=0
                #print(lines)
                if tempgene1!="":
                    #print(tempdict2)
                    for item in dict1:
                        tempcount1+=1
                        if tempdict3[0:2] == item[0:2] and tempdict3[-4:] == item[-4:]:
                            dict1[item]=dict1[item]+","+tempgene1
                            #print("True")
                            break
for item in wholelist1:
    #print(len(dict1[item]))
    tempcount2=0
    for x in dict1[item]:
        if x==",":
            tempcount2+=1
    if tempcount2==1:
        dict1[item]=dict1[item]+",NA"

#print(dict1)


with open("testnew.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
                #print(files)
            for lines in f1:
                count=0
                tempdict3=""
                tempgene=""
                tempgene3=""
                for word in lines.split(","):
                    if count==0 and "mycali" not in files and "caliReports" not in files:
                        if word=="Gene":
                            break
                        if "mycali" not in files and "caliReports" not in files:
                            tempdict3=files[files.find("/")+1:files.find("_")]
                            #print(tempdict1)
                    if count==0 and "mycali" not in files and "caliReports" not in files:
                        tempdict1+=","
                        if word=="mitochondrial_genome":
                            tempdict3+="CYTOb"
                        else:tempdict3+=word
                    if count==5 and "mycali" not in files and "caliReports" not in files:
                        tempdict3+=(","+word)
                    if count==6 and "mycali" not in files and "caliReports" not in files:
                        tempgene=word
                        #print(tempgene)
                    if count==7 and "mycali" not in files and "caliReports" not in files:
                        tempdict3+=word
                        tempdict3+=tempgene
                    if count==10 and "mycali" not in files and "caliReports" not in files:
                        tempgene3=word
                        #print(tempgene3)
                    count+=1
                tempcount=0
                if tempgene3!="":
                    for item in dict1:
                        tempcount+=1
                        if tempdict3[0:2] == item[0:2] and tempdict3[-4:] == item[-4:]:
                            #print(tempgene3)
                            #if item =="MRA-1236,K13,C469C":
                                #print(tempdict3)
                                #print("True")
                            if "Major" not in dict1[item]:
                                dict1[item]=dict1[item]+","+tempgene3
                                break
for item in wholelist1:
    #print(len(dict1[item]))
    tempcount3=0
    for x in dict1[item]:
        if x==",":
            tempcount3+=1
    if tempcount3==2:
        #print("True")
        dict1[item]=dict1[item]+",NA"

with open("testnew.csv", 'w') as t1:
    t1.write("Sample,Gene,SNP,NeST,NeST(my),NFNeST"+"\n")
    for item in dict1:
        t1.write(item+dict1[item]+"\n")

