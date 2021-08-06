import csv

import os
import re
with open("formatnew1.csv", 'w') as t1:
    writer = csv.writer(t1)
    writer.writerow(
        [None,"dhps_reportable1","dhps_reportable2","dhps_reportable3","dhps_reportable4","dhps_reportable5",None,"dhfr_reportable1","dhfr_reportable2","dhfr_reportable3","dhfr_reportable4","dhfr_reportable5",None,"Pfcrt_reportable1","Pfcrt_reportable2","Pfcrt_reportable3","Pfcrt_reportable4","Pfcrt_reportable5","Pfcrt_reportable6","Pfcrt_reportable7","Pfcrt_reportable8","Pfcrt_reportable9","Pfcrt_reportable10","Pfcrt_reportable11","Pfcrt_reportable12","Pfcrt_reportable13","Pfcrt_reportable14","Pfcrt_reportable15","Pfcrt_reportable16","Pfcrt_reportable17",None,"MDR_reportable1","MDR_reportable2","MDR_reportable3","MDR_reportable4","MDR_reportable5", None,"cytob_reportable1", "cytob_reportable2", None,"K13_reportable1","K13_reportable2","K13_reportable3","K13_reportable4","K13_reportable5","K13_reportable6","K13_reportable7","K13_reportable8","K13_reportable1","K13_reportable9","K13_reportable10","K13_reportable11","K13_reportable12","K13_reportable13","K13_reportable14","K13_reportable15","K13_reportable16","K13_reportable17","K13_reportable18","K13_reportable19","K13_reportable20","K13_reportable21","K13_reportable22","K13_reportable23"])
    writer.writerow(
        ["Sample Name","S436A","A437G","K540E","A581G","A613S",None,"A16V", "N51I", "C59R", "S108N", "I164L", None, "K76T", "C72S", "V73V", "M74I", "N75E", "T93S", "H97Y", "F145I", "I218F", "A220S", "Q271E", "N326S", "M343L", "C350R", "G353V", "I356T", "R371I", None, "N86Y", "Y184F", "S1034C", "N1042D", "D1246Y", None,"I258M","Y268N",None,
"P441L","F446I","G449A","N458Y","C469F","C469Y","M476I","A481V","Y493H","R515K","P527H","N537I","G538V","R539T","I543T","P553L","R561H","V568G","P574L","A578S","C580Y","D584V","R622I","A675V"])

list1=["S436A","A437G","K540E","A581G","A613S","A16V", "N51I", "C59R", "S108N", "I164L", "K76T", "C72S", "V73V", "M74I", "N75E", "T93S", "H97Y", "F145I", "I218F", "A220S", "Q271E", "N326S", "M343L", "C350R", "G353V", "I356T", "R371I", "N86Y", "Y184F", "S1034C", "N1042D", "D1246Y","I258M","Y268N",
"P441L","F446I","G449A","N458Y","C469F","C469Y","M476I","A481V","Y493H","R515K","P527H","N537I","G538V","R539T","I543T","P553L","R561H","V568G","P574L","A578S","C580Y","D584V","R622I","A675V"]

    #t1.write("\t"+"dhps_reportable"+"\t"+"dhfr_reportable"+"\t"+"Pfcrt_reportable"+"\t"+"MDR_reportable"+"\t"+"cytob_reportable"+"\t"+"K13_reportable")
wholefiles=[]
for subdir, dirs, files in os.walk("Allreports10dom1"):
    for file in files:
        if "Domestic1Reports" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]

wholelist1=[]
dict1={}
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

dict2={}

for files in wholefiles:
        with open(files,"r") as f1:
                #print(files)
            #print(f1)
            if "Allreports10dom1" in files:
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
                        for item in wholelist1:
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
                            #print(tempgene1)
                                if item not in dict1:
                                    #print("True")
                                    #print(tempgene1)
                                    #print(tempgene1)
                                    dict1[item]=","+tempgene1
                                    dict2[item]=tempvafaf1
                                    break


dict3={}
for item in dict1:
    for item2 in list1:
        if item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::] in list1:
            if item[0:item.find(",")] not in dict3:
                dict3[item[0:item.find(",")]]=item[0:item.find(",")]
            dict3[item[0:item.find(",")]]=dict3[item[0:item.find(",")]]+dict2[item]
            print(item[0:item.find(",")])
            print(item[item.find(",")+1:item.find(",")+1+item[item.find(",")+1::].find(",")])
            print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::])
            print(dict2[item])
        else:
            if item[0:item.find(",")] not in dict3:
                dict3[item[0:item.find(",")]]=item[0:item.find(",")]
            dict3[item[0:item.find(",")]]=dict3[item[0:item.find(",")]]+" "

print(dict3)


dict3={}
for item in dict1:
    for item2 in list1:
        if item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::] in list1:
            if item[0:item.find(",")] not in dict3:
                dict3[item[0:item.find(",")]]=item[0:item.find(",")]
            dict3[item[0:item.find(",")]]=dict3[item[0:item.find(",")]]+dict2[item]
            print(item[0:item.find(",")])
            print(item[item.find(",")+1:item.find(",")+1+item[item.find(",")+1::].find(",")])
            print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::])
            print(dict2[item])
        else:
            if item[0:item.find(",")] not in dict3:
                dict3[item[0:item.find(",")]]=item[0:item.find(",")]
            dict3[item[0:item.find(",")]]=dict3[item[0:item.find(",")]]+" "

print(dict3)
