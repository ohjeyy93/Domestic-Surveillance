import csv
import os
import re

with open("domesticformat1.csv", 'w') as t1:
    writer = csv.writer(t1)
    writer.writerow(
        [None,"dhps_reportable1","dhps_reportable2","dhps_reportable3","dhps_reportable4","dhps_reportable5",None,"dhfr_reportable1","dhfr_reportable2","dhfr_reportable3","dhfr_reportable4","dhfr_reportable5",None,"Pfcrt_reportable1","Pfcrt_reportable2","Pfcrt_reportable3","Pfcrt_reportable4","Pfcrt_reportable5","Pfcrt_reportable6","Pfcrt_reportable7","Pfcrt_reportable8","Pfcrt_reportable9","Pfcrt_reportable10","Pfcrt_reportable11","Pfcrt_reportable12","Pfcrt_reportable13","Pfcrt_reportable14","Pfcrt_reportable15","Pfcrt_reportable16","Pfcrt_reportable17",None,"MDR_reportable1","MDR_reportable2","MDR_reportable3","MDR_reportable4","MDR_reportable5", None,"cytob_reportable1", "cytob_reportable2", None,"K13_reportable1","K13_reportable2","K13_reportable3","K13_reportable4","K13_reportable5","K13_reportable6","K13_reportable7","K13_reportable8","K13_reportable1","K13_reportable9","K13_reportable10","K13_reportable11","K13_reportable12","K13_reportable13","K13_reportable14","K13_reportable15","K13_reportable16","K13_reportable17","K13_reportable18","K13_reportable19","K13_reportable20","K13_reportable21","K13_reportable22","K13_reportable23"])
    writer.writerow(
        ["Sample Name","S436A","A437G","K540E","A581G","A613S",None,"A16V", "N51I", "C59R", "S108N", "I164L", None, "K76T", "C72S", "V73V", "M74I", "N75E", "T93S", "H97Y", "F145I", "I218F", "A220S", "Q271E", "N326S", "M343L", "C350R", "G353V", "I356T", "R371I", None, "N86Y", "Y184F", "S1034C", "N1042D", "D1246Y", None,"I258M","Y268N",None,
"P441L","F446I","G449A","N458Y","C469F","C469Y","M476I","A481V","Y493H","R515K","P527H","N537I","G538V","R539T","I543T","P553L","R561H","V568G","P574L","A578S","C580Y","D584V","R622I","A675V"])

list1=["S436A","A437G","K540E","A581G","A613S","None","A16V", "N51I", "C59R", "S108N", "I164L", "None", "K76T", "C72S", "V73V", "M74I", "N75E", "T93S", "H97Y", "F145I", "I218F", "A220S", "Q271E", "N326S", "M343L", "C350R", "G353V", "I356T", "R371I", "None", "N86Y", "Y184F", "S1034C", "N1042D", "D1246Y", "None","I258M","Y268N","None",
"P441L","F446I","G449A","N458Y","C469F","C469Y","M476I","A481V","Y493H","R515K","P527H","N537I","G538V","R539T","I543T","P553L","R561H","V568G","P574L","A578S","C580Y","D584V","R622I","A675V"]

    #t1.write("\t"+"dhps_reportable"+"\t"+"dhfr_reportable"+"\t"+"Pfcrt_reportable"+"\t"+"MDR_reportable"+"\t"+"cytob_reportable"+"\t"+"K13_reportable")
wholefiles=[]
for subdir, dirs, files in os.walk("Allreports11dom2"):
    for file in files:
        if "Domestic1Reports" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]

#print(len(wholefiles))
wholelist1=[]
dict1={}
dict2={}
dictwd={}
for files in wholefiles:
    with open(files,"r") as f1:
        #print(files)
        for lines in f1:
            count=0
            tempdict1=""
            tempgene1=""
            tempgene2=""
            tempvafdp1=""
            #print(lines)
            for word in lines.split(","):
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
                if count==9 and "Domestic1Reports" not in files:
                    tempvafdp1=word
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
                #print(tempdict1)
                #print(test2)
                #if test2[0]!=test2[-1]:
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
                            #print(tempdict1)
                            #print(tempdict1)
                            wholelist1+=[tempdict1]
                            dict2[tempdict1]=tempvafdp1
                            #print(item)
                            dictwd[tempdict1]="WT"


dict3={}
dictwd2={}
#print(len(dict1))
for item in dict2:
    #if item[0:item.find(",")] not in dict3:
        #dict3[item[0:item.find(",")]]=item[0:item.find(",")]
    #print(dict2[item])
    #print(dict2[item])
    #print(item in dict2)
    dict3[item[0:item.find(",")],item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]]=dict2[item]
    dictwd2[item[0:item.find(",")],item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]]=dictwd[item]
        #print(item[0:item.find(",")])
        #print(item[item.find(",")+1:item.find(",")+1+item[item.find(",")+1::].find(",")])
    #    print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::])
    #    print(dict2[item])
    #else:dict3[item[0:item.find(",")]]=item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]+dict2[item]
dict5={}
dict6={}
for item in wholelist1:
    #print(item)
    #print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::])
    if item[0:item.find(",")] not in dict5:
        dict5[item[0:item.find(",")]]=item[0:item.find(",")]
        dict6[item[0:item.find(",")]]=item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]
        #dict4[item[0:item.find(",")]]=dict4[item]
#print(dictwd2)
#print(dict5)
#print(dict3)
#print(dict6)
#print(dictwd2)
dict4={}
#print(len(dict5))
#print(len(list1))
#print(len(dictwd2))
#print(len(wholelist1))
#print(len(list1))
#print(dictwd2)
#print(len(dict5))
for item in dict5:     
    #print(item)
    for item2 in list1:
        #print(item2)
        #print(dict6[item])
        if item not in dict4:
            dict4[item]=item
        if item2!="None":
            if (item,item2) in dict3:
                #print("True")
                #print(dict3[item,dict6[item]])
                #print(dict3[item,dict6[item]])
                #print(dict3[item,item2])
                if (dict3[item,item2])!='NA':
                    #print(item,dict6[item])
                    #print("True")
                    dict4[item]=dict4[item]+","+str(float(dict3[item,item2])*100)+"%"
                if (dict3[item,item2])=='NA':
                    dict4[item]=dict4[item]+","+"None"
            else:
                #print(dict4[item])
                item3=item2[0:-1]+item2[0]
                #print(item2[0:-1])
                #print(item3)
                #print(item2[::-1])
                #print(item3)
                if (item,item3) in dictwd2:
                    #print("TRUE")
                    if dictwd2[item,item3] == "WT":
                        #print(dictwd2[item,item3])
                        dict4[item]=dict4[item]+","+"WT"
                    else:
                        dict4[item]=dict4[item]+","+"None"
                else:
                    dict4[item]=dict4[item]+","+"None"
        if item2=="None":
            dict4[item]=dict4[item]+","+" "
                #print("true")

#print(dict4)
#print(len(list1))
print(len(dict5))
print(len(dict4))
sortednames=sorted(dict4.keys(), key=lambda x:x.lower())

for item in sortednames:
    #print(dict4[item])
    #print(type(lisdict4[item]))
    #print(dict4[])
    with open("domesticformat1.csv", 'a') as t1:
        writer = csv.writer(t1)
        writer.writerow(list(dict4[item].split(",")))

#print(dict3)
