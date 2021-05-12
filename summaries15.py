import os
import re

wholefiles=[]
for subdir, dirs, files in os.walk("Allreports5nor1"):
    for file in files:
        if "cali" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]
        if "cali" in subdir:
            if "known_variants.csv" in file:
                wholefiles+=[os.path.join(subdir, file)]

for subdir, dirs, files in os.walk("Allreports5cov1"):
    for file in files:
        if "cali" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]
        if "cali" in subdir:
            if "known_variants.csv" in file:
                wholefiles+=[os.path.join(subdir, file)]

for subdir, dirs, files in os.walk("Allreports5bb"):
    for file in files:
        if "cali" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]
        if "cali" in subdir:
            if "known_variants.csv" in file:
                wholefiles+=[os.path.join(subdir, file)]

for subdir, dirs, files in os.walk("Allreports5lowcov"):
    for file in files:
        if "cali" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]
        if "cali" in subdir:
            if "known_variants.csv" in file:
                wholefiles+=[os.path.join(subdir, file)]


#print(wholefiles)

wholelist1=[]
dict1={}
with open("testnew2.csv", 'w') as t1:
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
                    if (count==3 and "mycali" in files) or (count==3 and "caliReports" in files) or (count==3 and "replicalieports" in files):
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
                    if (count==4 and "mycali" in files) or (count==4 and "caliReports" in files) or (count==4 and "replicalieports" in files):
                        #print(word)
                        #print(lines)
                        tempdict1+=","
                        tempdict1+=word
                    if count==5:
                        if word=="AAref":
                            tempdict1=""
                            break
                    if count==5 and "mycali" not in files and "caliReports" not in files and "replicalieports" not in files:
                        tempdict1+=(","+word)
                    if count==6 and "mycali" not in files and "caliReports" not in files and "replicalieports" not in files:
                        tempgene=word
                    if count==7 and "mycali" not in files and "caliReports" not in files and "replicalieports" not in files:
                        tempdict1+=word
                        tempdict1+=tempgene
                        #print(lines)
                        #print(tempdict1)
                    if count==0:
                        if word=="Sample":
                            break
                        if "mycali" in files or "caliReports" in files or "replicalieports" in files:
                            if word.find("_")!=-1 and "mitochondrial" not in word:
                                tempdict1=word[0:word.find("_")]
                                #print(tempdict1)
                        if "mycali" not in files and "caliReports" not in files and "replicalieports" not in files:
                            tempdict1=files[files.find("/")+1:files.find("_")]
                            #print(tempdict1)
                    if count==0 and "mycali" not in files and "caliReports" not in files and "replicalieports" not in files:
                        tempdict1+=","
                        if word=="mitochondrial_genome":
                            tempdict1+="CYTOb"
                        else:tempdict1+=word
                    count+=1
                tempcount=0
                if tempdict1!="":
                    test1=tempdict1[tempdict1.find(",")+1::]
                    test2=test1[test1.find(",")+1::]
                #print(test1[test1.find(",")+1::])
                    if test2[0]!=test2[-1]:
                    #print(tempdict1[0:2])
                        if wholelist1==[] and tempdict1!='':
                            wholelist1+=[tempdict1]
                        if tempdict1!="":
                            for item in wholelist1:
                                tempcount+=1
                                if tempdict1[0:2] == item[0:2] and tempdict1[-5:-1] == item[-5:-1]:
                                    break
                                if tempcount==len(wholelist1):
                                    #print(tempdict1[tempdict1.find(",")+1::])
                                    #print(tempdict1[(tempdict1[tempdict1.find(",")+1::]).find(",")+1::])
                                    #print(test1[test1.find(",")+1::])
                                    wholelist1+=[tempdict1]
#print(wholelist1)

with open("semi1.csv", "r") as r1:
    for lines in r1:
        count=0
        templist1=""
        for word in lines.split(","):
            if count==0:
                templist1+=word
            elif count<3:
                templist1+=","+word
            count+=1
        if templist1 not in wholelist1:
            wholelist1+=[templist1]

with open("testnew2.csv", 'w') as t1:
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


with open("testnew2.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
            for lines in f1:
                count=0
                tempdict3=""
                tempgene1=""
                for word in lines.split(","):
                    if count==0 and "replicalieports" in files:
                        if word=="Sample":
                            break
                        if word.find("_")!=-1 and "mitochondrial" not in word:
                            tempdict3=word[0:word.find("_")]
                                #print(tempdict1)
                            #print(tempdict1)
                    if (count==3 and "replicalieports" in files):
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
                    if (count==4 and "replicalieports" in files):
                        #print(word)
                        #print(lines)
                        tempdict3+=","
                        tempdict3+=word
                        #print(tempdict1)
                        #print(tempdict1)
                    if count==5 and "replicalieports" in files:
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



with open("testnew2.csv", 'w') as t1:
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
    if tempcount2==2:
        dict1[item]=dict1[item]+",NA"

#print(dict1)


with open("testnew2.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
                #print(files)
            if "Allreports5nor1" in files:
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
                    #print(tempdict3[-5:-1])
                    if tempgene3!="":
                        for item in dict1:
                            tempcount+=1
                            if tempdict3[0:2] == item[0:2] and tempdict3[-5:-1] == item[-5:-1]:
                                #print(tempgene3)
                                #if item =="MRA-1236,K13,C469C":
                                    #print(tempdict3)
                                    #print("True")
                                a=dict1[item].split(",")
                                #print(len(a))
                                if len(a)==4:
                                    dict1[item]=dict1[item]+","+tempgene3
                                    break
for item in wholelist1:
    #print(len(dict1[item]))
    tempcount3=0
    for x in dict1[item]:
        if x==",":
            tempcount3+=1
    if tempcount3==3:
        #print("True")
        dict1[item]=dict1[item]+",NA"

#print(dict1)


with open("testnew2.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
                #print(files)
            if "Allreports5cov1" in files:
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
                    tempcount2=0
                    if tempgene3!="":
                        for item in dict1:
                            tempcount+=1
                            if tempdict3[0:2] == item[0:2] and tempdict3[-5:-1] == item[-5:-1]:
                                #print(tempgene3)
                                #if item =="MRA-1236,K13,C469C":
                                    #print(tempdict3)
                                    #print("True")
                                a=dict1[item].split(",")
                                if len(a)==5:
                                    dict1[item]=dict1[item]+","+tempgene3
                                    break
for item in wholelist1:
    #print(len(dict1[item]))
    tempcount3=0
    for x in dict1[item]:
        if x==",":
            tempcount3+=1
    if tempcount3==4:
        #print("True")
        dict1[item]=dict1[item]+",NA"


with open("testnew2.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
                #print(files)
            if "Allreports5bb" in files:
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
                    tempcount2=0
                    if tempgene3!="":
                        for item in dict1:
                            tempcount+=1
                            if tempdict3[0:2] == item[0:2] and tempdict3[-5:-1] == item[-5:-1]:
                                #print(tempgene3)
                                #if item =="MRA-1236,K13,C469C":
                                    #print(tempdict3)
                                    #print("True")
                                a=dict1[item].split(",")
                                if len(a)==6:
                                    dict1[item]=dict1[item]+","+tempgene3
                                    break
for item in wholelist1:
    #print(len(dict1[item]))
    tempcount3=0
    for x in dict1[item]:
        if x==",":
            tempcount3+=1
    if tempcount3==5:
        #print("True")
        dict1[item]=dict1[item]+",NA"

with open("testnew2.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
                #print(files)
            if "Allreports5lowcov" in files:
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
                    tempcount2=0
                    if tempgene3!="":
                        for item in dict1:
                            tempcount+=1
                            if tempdict3[0:2] == item[0:2] and tempdict3[-5:-1] == item[-5:-1]:
                                #print(tempgene3)
                                #if item =="MRA-1236,K13,C469C":
                                    #print(tempdict3)
                                    #print("True")
                                a=dict1[item].split(",")
                                if len(a)==7:
                                    dict1[item]=dict1[item]+","+tempgene3
                                    break
for item in wholelist1:
    #print(len(dict1[item]))
    tempcount3=0
    for x in dict1[item]:
        if x==",":
            tempcount3+=1
    if tempcount3==6:
        #print("True")
        dict1[item]=dict1[item]+",NA"


wholefiles=[]
for subdir, dirs, files in os.walk("Geneioustables2"):
    for file in files:
        wholefiles+=[os.path.join(subdir, file)]

wholegenilist1=[]
for files in wholefiles:
    with open(files,"r") as f1:
        #print(files)
        count=0
        for lines in f1:
            count+=1
            #print(files[files.find("/")+1:files.find("_")])
            if count==1:
                countcom1=0
                countcom2=0
                pos1=lines.find("Amino Acid Change")+1
                pos2=lines.find("CDS Codon Number")+1
                countpos=0
                for word in lines:
                    countpos+=1
                    if word=="," and countpos<pos1:
                        countcom1+=1
                    if word=="," and countpos<pos2:
                        countcom2+=1
                #print(lines)
            if count!=1:
                tempword1=""
                tempword2=""
                tempcount=0
                for word in lines:
                    if word==",":
                        tempcount+=1
                    if tempcount==countcom1:
                        tempword1+=word
                    if tempcount==countcom2:
                        tempword2+=word
            if count!=1:
                #print(tempword1.find("->"))
                if len(tempword1[1::])==6 and tempword1.find("-")==3: #and tempword1[3:5]=="->":
                    #print(files[files.find("/")+1:files.find("_")])
                    for item in ["PfCRT","K13","PfMDR1","mitchondrial genome","DHFR","DHPS"]:
                        if item in files:
                            wholegenilist1+=[files[files.find("/")+1:files.find("_")]+","+item+","+tempword1[1]+tempword2[1::]+tempword1[-1]]

#print(wholegenilist1)
for item in wholelist1:
    #print(item)
    if item in wholegenilist1:
        #print(item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
        dict1[item]=dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::]
        #print("True")
        #dict1[item]=dict1[item]+",NA"
    else:
        dict1[item]=dict1[item]+",NA"


with open("semi1.csv", "r") as r1:
    for lines in r1:
        count=0
        templist1=""
        templist2=""
        for word in lines.split(","):
            if count==0:
                templist1+=word
            elif count<3:
                templist1+=","+word
            if count==3:
                templist2=word.strip("\n")
                #print(word)
            count+=1
        #print(count)
        #print(templist1)
        #print(templist2)
        #if templist2=="":
        #    print("True")
        #print(dict1[templist1]+","+templist2)
        #print(dict1[templist1]+","+templist2)
        #if templist1 not in wholelist1:
        #    print("True")
        if templist2!="N86F":
            dict1[templist1]=dict1[templist1]+","+templist2

for item in wholelist1:
    #print(len(dict1[item]))
    tempcount=0
    for x in dict1[item]:
        if x==",":
            tempcount+=1
    #print(tempcount)
    if tempcount==8:
        #print("True")
        dict1[item]=dict1[item]+",NA"


with open("testnew3.csv", 'w') as t1:
    t1.write("Sample,Gene,SNP,NeST(cali),NeST(2.0.0st),NeST(2.0.1),NFNeST,NFNeST(NoCov75%),NFNeST(bbduk1),NFNeST(lowcov),Geneious,Control"+"\n")
    for item in dict1:
        #print(item)
        if item=="Dd2,PfMDR1,N86Y":
            t1.write(item+dict1[item][:-5]+",N86F"+"\n")
        t1.write(item+dict1[item]+"\n")

