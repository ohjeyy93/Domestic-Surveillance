import os
import re

wholefiles=[]
for subdir, dirs, files in os.walk("Allreports6nor"):
    for file in files:
        if "Domestic1Reports" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]
        if "Domestic1Reports" in subdir:
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
                    if (count==3 and "Domestic1Reports" in files):
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
                    if (count==4 and "Domestic1Reports" in files):
                        #print(word)
                        #print(lines)
                        tempdict1+=","
                        tempdict1+=word
                    if count==5:
                        if word=="AAref":
                            tempdict1=""
                            break
                    if count==5 and "Domestic1Reports" not in files:
                        tempdict1+=(","+word)
                    if count==6 and "Domestic1Reports" not in files:
                        tempgene=word
                    if count==7 and "Domestic1Reports" not in files:
                        tempdict1+=word
                        tempdict1+=tempgene
                        #print(lines)
                        #print(tempdict1)
                    if count==0:
                        if word=="Sample":
                            break
                        if "Domestic1Reports" in files:
                            if word.find("_")!=-1 and "mitochondrial" not in word:
                                tempdict1=word[0:word.find("_")]
                                #print(tempdict1)
                        if "Domestic1Reports" not in files:
                            tempdict1=files[files.find("/")+1:files.find("_")]
                            #print(tempdict1)
                    if count==0 and "Domestic1Reports" not in files:
                        tempdict1+=","
                        if word=="mitochondrial_genome":
                            tempdict1+="CYTOb"
                        else:tempdict1+=word
                    count+=1
                tempcount=0
                #print(tempdict1)
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
                tempdict2=""
                tempgene1=""
                for word in lines.split(","):
                    if count==0 and "Domestic1Reports" in files:
                        #print(word)
                        if word=="Sample":
                            break
                        if word.find("_")!=-1 and "mitochondrial" not in word:
                            tempdict2=word[0:word.find("_")]
                                #print(tempdict1)
                            #print(tempdict1)
                    if (count==3 and "Domestic1Reports" in files):
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
                    if (count==4 and "Domestic1Reports" in files):
                        #print(word)
                        #print(lines)
                        tempdict2+=","
                        tempdict2+=word
                        #print(tempdict1)
                        #print(tempdict1)
                        #print(tempdict2)
                    if count==5 and "Domestic1Reports" in files:
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

with open("testnew2.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
                #print(files)
            #print(f1)
            if "Allreports6nor" in files:
                for lines in f1:
                    #print(lines)
                    count=0
                    tempdict3=""
                    tempgene=""
                    tempgene3=""
                    for word in lines.split(","):
                        #print(word)
                        if count==0 and "Domestic1Reports" not in files:
                            if word=="Gene":
                                break
                            if "Domestic1Reports" not in files:
                                tempdict3=files[files.find("/")+1:files.find("_")]
                                #print(tempdict1)
                        if count==0 and "Domestic1Reports" not in files:
                            tempdict3+=","
                            if word=="mitochondrial_genome":
                                tempdict3+="CYTOb"
                            else:tempdict3+=word
                        if count==5 and "Domestic1Reports" not in files:
                            tempdict3+=(","+word)
                        if count==6 and "Domestic1Reports" not in files:
                            tempgene=word
                            #print(tempgene)
                        #print(tempdict3)
                        if count==7 and "Domestic1Reports" not in files:
                            tempdict3+=word
                            tempdict3+=tempgene
                        if count==10 and "Domestic1Reports" not in files:
                            tempgene3=word
                            #print(tempgene3)
                        count+=1
                    #print(tempgene)
                    #print(tempgene3)
                    tempcount=0
                    #print(tempdict3[-5:-1])
                    #print(tempgene3)
                    #print(tempdict3)
                    #print(tempgene3)
                    if tempgene3!="":
                        for item in dict1:
                            tempcount+=1
                            #print(tempdict3)
                            #print(item)
                            #if "45" in tempdict3:
                            #    print(tempdict3)
                            #print(item)
                            #print(tempdict3)
                            if tempdict3[0:12] == item[0:12] and tempdict3[-10:-1] == item[-10:-1]:
                                #print(tempgene3)
                                #if item =="MRA-1236,K13,C469C":
                                    #print(tempdict3)
                                    #print("True")
                                #print(dict1[item])
                                #print(item, dict1[item], tempgene3)
                                a=dict1[item].split(",")
                                #print(dict1[item])
                                #print(a)
                                #print(len(a))
                                if len(a)==2:
                                    #if "45" in tempdict3:
                                        #print(tempdict3)
                                    #    print(item, dict1[item], tempgene3)
                                    #if "45" in tempdict3:
                                    #    print(item, tempgene3)
                                    #print(a)
                                    #print(tempgene3)
                                    #print(tempgene3)
                                    #print("true")
                                    #print(item,dict1[item],tempgene3)
                                    dict1[item]=dict1[item]+","+tempgene3
                                    break
#print(dict1)
#for item in dict1:
#    if "45" in item:
#        print(dict1[item])

for item in wholelist1:
    #print(len(dict1[item]))
    tempcount3=0
    for x in dict1[item]:
        if x==",":
            tempcount3+=1
    if tempcount3==1:
        #print("True")
        dict1[item]=dict1[item]+",NA"

#print(dict1)


wholefiles=[]
for subdir, dirs, files in os.walk("geneiousdomestic1"):
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
                #print(tempword1)
                if len(tempword1[1::])==6 and tempword1.find("-")==3: #and tempword1[3:5]=="->":
                    #print(files[files.find("/")+1:files.find("_")])
                    for item in ["PfCRT","K13","PfMDR1","mitchondrial genome","DHFR","DHPS"]:
                        if item in files:
                            wholegenilist1+=[files[files.find("/")+1:files.find("_")]+","+item+","+tempword1[1]+tempword2[1::]+tempword1[-1]]

#print(wholegenilist1)
for item in wholelist1:
    #print(item)
    if item in wholegenilist1:
        #print("true")
        #print(item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
        dict1[item]=dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::]
        #print("True")
        #dict1[item]=dict1[item]+",NA"
    else:
        dict1[item]=dict1[item]+",NA"


#print(dict1)
with open("testdom1.csv", 'w') as t1:
    t1.write("Sample,Gene,SNP,NeST(2.0.0st),NFNeST,Geneious"+"\n")
    for item in dict1:
        #print(item)
        if item=="Dd2,PfMDR1,N86Y":
            t1.write(item+dict1[item][:-5]+",N86F"+"\n")
        t1.write(item+dict1[item]+"\n")

