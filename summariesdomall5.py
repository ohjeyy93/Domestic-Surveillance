import os
import re

wholefiles=[]
for subdir, dirs, files in os.walk("Allreports11dom2"):
    for file in files:
        if "Domestic1Reports" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]

wholelist1=[]
dict1={}
dict2={}
dict3={}
dict4={}
for files in wholefiles:
    #print(files)
    #print(files)
    with open(files,"r") as f1:
        #print(files)
        for lines in f1:
            count=0
            tempdict1=""
            tempgene1=""
            tempgene2=""
            tempbasepos1=""
            #print(lines)
            for word in lines.split(","):
                if count==1: tempbasepos1=word
                if count==2: tempcov=word
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
                    #print(wholelist1)
                    for item in wholelist1:
                        #print(item)
                        tempcount+=1
                        if tempdict1[0:20] == item[0:20] and tempdict1[-10:-1] == item[-10:-1]:
                            break
                        if tempcount==len(wholelist1):
                            #print(item)
                            #print(tempdict1)
                            wholelist1+=[tempdict1]
                            #print(item)
                            #print(tempgene)
                            #if item not in dict1:
                            #    dict1[item]
                            #print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::])
                            #print(item)
                            if item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::][0]==item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::][-1]:
                                dict1[item]=item+",WT"
                            else:
                                dict1[item]=item+","+item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]
                            #print(dict1[item])
                            dict4[item]=tempbasepos1
                            dict2[item]=tempcov
                            dict3[item]=tempvafdp1 
dictgenes1={}
dictgenes1["DHPS"]=[436,437,540,581,613]
dictgenes1["DHFR"]=[16,51,59,108,164]
dictgenes1["PfCRT"]=[76,72,73,74,75,93,97,145,218,220,271,326,343,350,353,356,371]
dictgenes1["PfMDR1"]=[86,184,1034,1042,1246]
dictgenes1["CYTOb"]=[258,268]
dictgenes1["K13"]=[441,446,449,458,469,476,481,493,515,527,537,538,539,543,553,561,568,574,578,580,584,622,675]


dictgenes2={}
dictgenes2["DHPS",436]="S436A"
dictgenes2["DHPS",437]="A437G"
dictgenes2["DHPS",540]="K540E"
dictgenes2["DHPS",581]="A581G"
dictgenes2["DHPS",613]="A613S"
dictgenes2["DHFR",16]="A16V"
dictgenes2["DHFR",51]="N51I"
dictgenes2["DHFR",59]="C59R"
dictgenes2["DHFR",108]="S108N"
dictgenes2["DHFR",164]="I164L"
dictgenes2["PfCRT",76]="K76T"
dictgenes2["PfCRT",72]="C72S"
dictgenes2["PfCRT",73]="V73V"
dictgenes2["PfCRT",74]="M74I"
dictgenes2["PfCRT",75]="N75E"
dictgenes2["PfCRT",93]="T93S"
dictgenes2["PfCRT",97]="H97Y"
dictgenes2["PfCRT",145]="F145I"
dictgenes2["PfCRT",218]="I218F"
dictgenes2["PfCRT",220]="A220S"
dictgenes2["PfCRT",271]="Q271E"
dictgenes2["PfCRT",326]="N326S"
dictgenes2["PfCRT",343]="M343L"
dictgenes2["PfCRT",350]="C350R"
dictgenes2["PfCRT",353]="G353V"
dictgenes2["PfCRT",356]="I356T"
dictgenes2["PfCRT",371]="R371I"
dictgenes2["PfMDR1",86]="N86Y"
dictgenes2["PfMDR1",184]="Y184F"
dictgenes2["PfMDR1",1034]="S1034C"
dictgenes2["PfMDR1",1042]="N1042D"
dictgenes2["PfMDR1",1246]="D1246Y"
dictgenes2["CYTOb",258]="I258M"
dictgenes2["CYTOb",268]="Y268N"
dictgenes2["K13",441]="P441L"
dictgenes2["K13",446]="F446I"
dictgenes2["K13",449]="G449A"
dictgenes2["K13",458]="N458Y"
dictgenes2["K13",469]="C469F"
dictgenes2["K13",476]="M476I"
dictgenes2["K13",481]="A481V"
dictgenes2["K13",493]="Y493H"
dictgenes2["K13",515]="R515K"
dictgenes2["K13",527]="P527H"
dictgenes2["K13",537]="N537I"
dictgenes2["K13",538]="G538V"
dictgenes2["K13",539]="R539T"
dictgenes2["K13",543]="I543T"
dictgenes2["K13",553]="P553L"
dictgenes2["K13",561]="R561H"
dictgenes2["K13",568]="V568G"
dictgenes2["K13",574]="P574L"
dictgenes2["K13",578]="A578S"
dictgenes2["K13",580]="C580Y"
dictgenes2["K13",584]="D584V"
dictgenes2["K13",622]="R622I"
dictgenes2["K13",675]="A675V"

wholefiles=[]
for subdir, dirs, files in os.walk("geneiousannotationdomall1"):
    for file in files:
        wholefiles+=[os.path.join(subdir, file)]

wholegenilist1=[]
wholegenilistdic1={}
wholecovlist1={}
wholevaflist1={}
wholebplist1={}
for files in wholefiles:
    with open(files,"r") as f1:
        #print(files)
        count=0
        countcom1=0
        countcom2=0
        if files!="geneiousannotationdomall1/.DS_Store":
            for lines in f1:
                count=0
                current=""
                templist=""
                tempword=""
                templist2=""
                VF=""
                cov=""
                basepos1=""
                if lines.find("Polymorphism")!=-1 and lines.find("Polymorphism Type")==-1:
                    for word in lines.split(","):
                        if count==0:
                            for word2 in word.split(" "):
                                #print(word2[0:-6])
                                templist+=word2[0:-6]
                                break
                        if count==1:
                            #print(word)
                            templist+=","
                            if word=="mitochondrial genome - CYTB CDS":
                                templist+="CYTOb"
                            if word=="DHPS_437Corrected ":
                                templist+="DHPS"
                            if word=="PfMDR1 ":
                                templist+="PfMDR1"
                            if word!="mitochondrial genome - CYTB CDS" and word!="DHPS_437Corrected " and word!="PfMDR1 ":
                                templist+=word
                        #print(templist)
                        if count==19:
                            #print(templist)
                            #print(templist)
                            #print(templist[templist.find(",")+1::])
                            if int(word) in dictgenes1[templist[templist.find(",")+1::]]:
                                templist+=","+dictgenes2[templist[templist.find(",")+1::],int(word)]
                        #print(templist)
                        if count==17:
                            tempword=word
                        if count==21:
                            basepos1=word    
                        if count==27:
                            cov=word
                        if count==61:
                            VF=word
                        count+=1
                #if templist[0:templist.find(",")]=="SRR8950984":
                    #print(templist)
                if tempword!="":
                    if tempword[0:2]=="MN" and tempword[-2::]=="IE":
                        wholegenilist1+=[templist]
                        wholegenilist1+=[templist2]
                        wholecovlist1+=cov
                        wholevaflist1+=VF
                        wholebplist1+=basepos1
                    else:
                        wholegenilist1+=[templist]
                        wholecovlist1[templist]=cov
                        wholevaflist1[templist]=VF
                        wholebplist1[templist]=basepos1

#print(wholegenilist1)

#print(wholegenilist1)
wholecount=0
#print(wholegenilist1)
wholecombinedlist1=wholelist1
for item in wholegenilist1:
    if item not in wholelist1:
        wholecombinedlist1+=[item]

for item in wholecombinedlist1:
    #print(item)
    #print(item)
    if item in dict1 and item in wholegenilist1:
        #print("true")
        #print(item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
        #print(dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
        dict1[item]=dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::]
        dict4[item]=dict4[item]+","+wholebplist1[item]
        dict2[item]=dict2[item]+","+wholecovlist1[item]
        dict3[item]=dict3[item]+","+wholevaflist1[item]
        #print("True")
        #dict1[item]=dict1[item]+",NA"
    if item in dict1 and item not in wholegenilist1:
        #if "S533C" in item:
        dict1[item]=dict1[item]+",NA"
        dict4[item]=dict4[item]+","+"NA"
        dict2[item]=dict2[item]+","+"NA"
        dict3[item]=dict3[item]+","+"NA"
    if item not in dict1 and item in wholegenilist1:
        dict1[item]=item+"NA"+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::]
        dict4[item]=item+"NA"+wholebplist1[item]
        dict2[item]=item+"NA"+wholecovlist1[item]
        dict3[item]=item+"NA"+wholevaflist1[item]
    #wholecount+=1


#print(dict1)
with open("testdomsam13.csv", 'w') as t1:
    t1.write("Sample,Gene,SNP,NFNeST,Geneious"+"\n")
    for item in dict1:
        #print(item)
        if item=="Dd2,PfMDR1,N86Y":
                t1.write(item+dict1[item][:-5]+",N86F"+"\n")
        #print(item)
        #print(item[item.find(",")+1::].find(","))
        #print(item[item.find(",")+1:item.find(",")+item[item.find(",")+1::].find(",")])
        #print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::])
        t1.write(dict1[item]+"\n")
        t1.write(item[0:item.find(",")]+",basepos,"+item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]+","+dict4[item]+"\n")
        t1.write(item[0:item.find(",")]+",coverage,"+item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]+","+dict2[item]+"\n")
        t1.write(item[0:item.find(",")]+",Variant frequency,"+item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]+","+dict3[item]+"\n")

