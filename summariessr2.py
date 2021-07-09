import os
import re

wholefiles=[]
for subdir, dirs, files in os.walk("Allreport9SSR1"):
    for file in files:
        if "Domestic1Reports" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]
        if "Domestic1Reports" in subdir:
            if "known_variants.csv" in file:
                wholefiles+=[os.path.join(subdir, file)]

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
                                #print(tempdic1)
                                #print(tempdict1)
                        if "Domestic1Reports" not in files:
                            #print(files)
                            #files.find("/")+1+files[files.find("/")+1::].find("/")
                            tempdict1=files[files.find("/")+1:files.find("/")+1+files[files.find("/")+1::].find("/")]
                            #print(tempdict1)
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
                    #print(test2[0],test2[-1])   
                #print(test1[test1.find(",")+1::])
                    if test2[0]!=test2[-1]:
                    #print(tempdict1[0:2])
                        if wholelist1==[] and tempdict1!="":
                            wholelist1+=[tempdict1]
                        if tempdict1!="":
                            for item in wholelist1:
                                tempcount+=1
                                if tempdict1[0:20] == item[0:20] and tempdict1[-10:-1] == item[-10:-1]:
                                    break
                                if tempcount==len(wholelist1):
                                    #print(tempdict1[tempdict1.find(",")+1::])
                                    #print(tempdict1[(tempdict1[tempdict1.find(",")+1::]).find(",")+1::])
                                    #print(test1[test1.find(",")+1::])
                                    #print(tempdict1)
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

#for x in wholelist1:
#    if "20CDAZxxx0016PfB1290" in x:
#        print(x)

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
                        #print(tempdict2)
                        #print(item)
                        if tempdict2[0:20] == item[0:20] and tempdict2[-10:-1] == item[-10:-1]:
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
dict2={}
dict3={}
dict4={}
with open("testnew2.csv", 'w') as t1:
    for files in wholefiles:
        with open(files,"r") as f1:
                #print(files)
            #print(f1)
            if "Allreport9SSR1" in files:
                for lines in f1:
                    #print(lines)
                    count=0
                    tempdict3=""
                    tempgene=""
                    tempgene3=""
                    tempcov=""
                    tempvafdp1=""
                    tempvafaf1=""
                    for word in lines.split(","):
                        #print(word)
                        if count==0 and "Domestic1Reports" not in files:
                            if word=="Gene":
                                break
                            if "Domestic1Reports" not in files:
                                tempdict3=files[files.find("/")+1:files.find("/")+1+files[files.find("/")+1::].find("/")]
                                #print(tempdict1)
                        if count==0 and "Domestic1Reports" not in files:
                            tempdict3+=","
                            if word=="mitochondrial_genome":
                                tempdict3+="CYTOb"
                            else:tempdict3+=word
                        if count==2: tempcov=word
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
                            tempvafdp1=word
                        if count==11 and "Domestic1Reports" not in files:
                            tempvafaf1=word
                        if count==12 and "Domestic1Reports" not in files:
                            tempgene3=word
                            #print(tempgene3)
                        count+=1
                    #print(tempgene)
                    #print(tempgene3)
                    tempcount=0
                    #print(tempdict3[-5:-1])
                    #print(tempgene3)
                    if tempgene3!="":
                        for item in dict1:
                            #print(item)
                            tempcount+=1
                            #print(tempdict3)
                            #print(item)
                            #if "45" in tempdict3:
                            #    print(tempdict3)
                            #print(item)
                            #print(tempdict3)
                            if tempdict3[0:20] == item[0:20] and tempdict3[-10:-1] == item[-10:-1]:
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
                                #if "20xxxxxxx0048PfB1290,DHPS" in tempdict3:
                                        #print(tempdict3)
                                #        print(tempgene3)
                                #        print(dict1[item    ])
                                #        print(a)
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
                                    dict2[item]=tempcov
                                    dict3[item]=tempvafdp1
                                    dict4[item]=tempvafaf1
                                    break

for item in wholelist1:
    #print(len(dict1[item]))
    tempcount3=0
    for x in dict1[item]:
        if x==",":
            tempcount3+=1
    if tempcount3==1:
        #print("True")
        dict1[item]=dict1[item]+",NA"
        dict2[item]="NA"
        dict3[item]="NA"
        dict4[item]="NA"        

wholefiles=[]
for subdir, dirs, files in os.walk("geneiousannotation1"):
    for file in files:
        wholefiles+=[os.path.join(subdir, file)]

wholegenilist1=[]
for files in wholefiles:
    with open(files,"r") as f1:
        #print(files)
        count=0
        countcom1=0
        countcom2=0
        if files!="geneiousannotation1/.DS_Store":
            for lines in f1:
                count=0
                current=""
                templist=""
                tempword=""
                templist2=""
                if lines.find("Polymorphism")!=-1:
                    for word in lines.split(","):
                        if count==0:
                            for word2 in word.split(" "):
                                templist+=word2
                                break
                        if count==17:
                            tempword=word
                        if count==19:
                            #if templist[::]=="SRR8950984":
                                #print(word)
                            for word2 in word.split(" "):
                                if word2.find("-TS")==-1:
                                    templist+=","+word2
                                if word2.find("-TS")!=-1:
                                    #if templist[::]=="SRR8950984":
                                        #print(word2[0:word2.find("-TS")])
                                    templist+=","+word2[0:word2.find("-TS")]     
                                break
                        if count==20 and tempword!="":
                            #print(tempword[0])
                            #print(tempword[-1])
                            #print(tempword[0:2])
                            #print(tempword[-2::])
                            if tempword[0:2]=="MN" and tempword[-2::]=="IE":
                                templist2=templist+","+tempword[1]+"75"+tempword[-1]
                                templist+=","+tempword[0]+word+tempword[-2]
                            else:templist+=","+tempword[0]+word+tempword[-1]
                        count+=1
                #if templist[0:templist.find(",")]=="SRR8950984":
                    #print(templist)
                if tempword!="":
                    if tempword[0:2]=="MN" and tempword[-2::]=="IE":
                        wholegenilist1+=[templist]
                        wholegenilist1+=[templist2]
                    else:wholegenilist1+=[templist]

#print(wholegenilist1)

#print(wholegenilist1)
for item in wholelist1:
    #print(item)
    if item in wholegenilist1:
        #print("true")
        #print(item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
        #print(dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
        dict1[item]=dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::]
        #print("True")
        #dict1[item]=dict1[item]+",NA"
    else:
        if "S533C" in item:
            dict1[item]=dict1[item]+",WT"
        else: dict1[item]=dict1[item]+",WT"


#print(dict1)
with open("testssr12.csv", 'w') as t1:
    t1.write("Sample,Gene,SNP,NeST(2.0.0st),NFNeST(SSR),Geneious"+"\n")
    for item in dict1:
        #print(item)
        if item=="Dd2,PfMDR1,N86Y":
            t1.write(item+dict1[item][:-5]+",N86F"+"\n")
        t1.write(item+dict1[item]+"\n")
        t1.write(item+","+","+dict2[item]+"\n")
        t1.write(item+","+","+dict3[item]+"\n")
        t1.write(item+","+","+dict4[item]+"\n")

