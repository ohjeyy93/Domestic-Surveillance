import os
import re
import operator
import csv

wholefiles=[]
for subdir, dirs, files in os.walk("Allreports11dom6"):
    for file in files:
        if "Domestic1Reports" not in subdir and "DS_Store" not in file:
            wholefiles+=[os.path.join(subdir, file)]

wholelist1=[]
dict1={}
dict2={}
dict3={}
dict4={}
dict1f={}
dict2f={}
dict3f={}
dict4f={}
dictvar={}
dictall={}
dictall2={}
dictvarbegin={}
dictvarend={}
wholevarlist1=[]
whoelistcut1=[]
dict751={}
for files in wholefiles:
    #print(files)
    #print(files)
    with open(files,"r") as f1:
        #print(files)
        count75=0
        for lines in f1:
            count=0
            tempdict1=""
            tempgene1=""
            tempgene2=""
            tempbasepos1=""
            #print(lines)
            for word in lines.split(","):
                if count==0:
                    if word=="Sample":
                        break
                    if word=="Gene":
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
                if count==1: tempbasepos1=word
                if count==2: tempcov=word
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
                count+=1
            tempcount=0
            #if "18xxxx00x07G8PfD1190_S28_L001" in files:
            #    print(tempdict1)
            #print(tempdict1)
            #if "19NGMOxxxx0163PfB1280_S27_L001" in files:
            #    print(lines)
            #    print(tempbasepos1)
            #    print(tempcov)
            if tempdict1!="" and tempcov!="NA":
                #if wholelist1==[] and tempdict1!="":
                #    wholelist1+=[tempdict1]
                #if tempdict1!="":
                    #print(wholelist1)
                #for item in wholelist1:
                    #print(item)
                    #tempcount+=1
                    #if tempdict1[0:20] == item[0:20] and tempdict1[-10:-1] == item[-10:-1]:
                    #    break
                    #if tempcount==len(wholelist1)+1:
                        #print(item)
                        #print(tempdict1)
                #print(tempdict1)
                wholelist1+=[tempdict1]
                whoelistcut1+=[tempdict1[0:-1]]
                dictall[tempdict1[0:-1]]="test"
                dictall2[tempdict1]="test"
                item=tempdict1
                #print(item)
                #print(item)
                #print(tempgene)
                #if item not in dict1:
                #    dict1[item]
                #print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::])
                #print(item)
                #if "18xxxx00x07G8PfD1190_S28_L001" in item:
                    #print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::][0])
                    #print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::][-1])
                #if "20CDNVxxx0003PfB1290_S3_L001" in item:
                #    print(item)
                #print(item)
                #####################################
                #if "N75" in tempdict1:
                #    count75+=1
                #    if count75==2:
                #        print(item)
                #        print(tempbasepos1)
                #        dictall[dict1[item[0:-1]]]=str(float(tempvafdp1)*100)+"%"
                ####################################
                if item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::][0]==item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::][-1]:
                    dict1[item[0:-1]]=item+",WT"
                    dictall[item[0:-1]]="WT"
                    dict1f[item]=item+",WT"
                    #if "18xxxx00x07G8PfD1190_S28_L001" in item:
                    #    print(dict1[item])
                else:
                    if item[0:-1] in dict1:
                        dict751[item[0:-1]]="test"
                        #dict1[item[0:-1]]=dict1[item[0:-1]]+","+item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]
                        #print(dict1[item[0:-1]])
                        #dictall[dict1[item[0:-1]]+","+item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]]=str(float(tempvafdp1)*100)+"%"
                        #print(dict1[item[0:-1]])
                        #wholelist1+=dict1[item[0:-1]]
                    dict1[item[0:-1]]=item+","+item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]
                    dict1f[item]=item+","+item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]
                    if tempvafdp1 == "NA":
                        dictvar[item[0:-1]]="NA"
                        dictall[item[0:-1]]="NA"
                    else:
                        dictvar[item[0:-1]]=str(float(tempvafdp1)*100)+"%"
                        dictall[item[0:-1]]=str(float(tempvafdp1)*100)+"%"
                    dictvarbegin[item[0:-1]]=item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::][0:-1]
                    dictvarend[item[0:-1]]=item[-1]
                #print(dict1[item])
                    #if "18xxxx00x07G8PfD1190_S28_L001" in item:
                    #    print(item)
                #    print(lines)
                #    print(tempbasepos1)
                #    print(tempcov)
                dict4[item[0:-1]]=tempbasepos1
                dict2[item[0:-1]]=tempcov
                dict4f[item]=tempbasepos1
                dict2f[item]=tempcov
                #print(tempvafdp1)
                if tempvafdp1!="NA":
                    dict3[item[0:-1]]=str(float(tempvafdp1)*100)+"%"
                    dict3f[item]=str(float(tempvafdp1)*100)+"%"
                if tempvafdp1=="NA":
                    dict3[item[0:-1]]=tempvafdp1
                    dict3f[item]=tempvafdp1
                        #if "19NGMOxxxx0163PfB1280_S27_L001" in files:
                        #    print(item)
                        #    print(tempbasepos1)
                        #    print(tempcov)
                        #    print(tempvafdp1)


#print(dict1["SRR8950949,DHPS,S436"])
#print(dict2["SRR8950949,DHPS,S436"])
#print(dict3["SRR8950949,DHPS,S436"])
#print(dict4["SRR8950949,DHPS,S436"])


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
for subdir, dirs, files in os.walk("geneiousannotationdomall4"):
    for file in files:
        wholefiles+=[os.path.join(subdir, file)]

wholegenilistcut1=[]
wholegenilist1=[]
wholegenilistdic1={}
wholecovlist1={}
wholevaflist1={}
wholebplist1={}
wholetypelist1={}
dict752={}

wholecovlist1f={}
wholevaflist1f={}
wholebplist1f={}
wholetypelist1f={}

#pfcrtdict2={}
for files in wholefiles:
    with open(files,"r") as f1:
        #print(files)
        count=0
        countcom1=0
        countcom2=0
        if files!="geneiousannotationdomall4/.DS_Store":
            for lines in f1:
                count=0
                current=""
                templist=""
                tempword=""
                templist2=""
                templist3=""
                tempseq1=""
                VF=""
                VRF=""
                cov=""
                basepos1=""
                tempAA1=""
                if lines.find("Polymorphism")!=-1 and lines.find("Polymorphism Type")==-1 and lines.find("Deletion")==-1 and lines.find("Insertion")==-1:
                    if lines.find("M74I")!=-1 and lines.find("transversion")!=-1 and lines.find("Substitution")!=-1:
                        continue
                    else:
                        #print(lines)
                        for word in lines.split(","):
                            #if word == "GAA":
                                #print(lines)
                            if count==0:
                                for word2 in word.split(" "):
                                    #print(word2[0:-6])
                                    templist+=word2
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
                            if count==4:
                                if len(word)>1:
                                    tempseq1=word
                            if count==16:
                                if word!="":
                                    tempAA1=word
                                    #if "19xxTXxxxx0204PfB1280_S63_L001" in templist:
                                    #        print(tempAA1)
                            if count==20:
                                #print(templist)
                                #print(templist)
                                #print(templist[templist.find(",")+1::])
                                #print(templist)
                                if word!="":
                                    if tempAA1!="":
                                        templist+=","+tempAA1[0]+word+tempAA1[-1]
                                        #if "19xxTXxxxx0204PfB1280_S63_L001" in templist:
                                        #    print(templist)
                                        #print(len(list(templist.split(","))))
                                    if len(list(templist.split(",")))<3 and int(word) in dictgenes1[templist[templist.find(",")+1::]] and tempAA1=="":
                                        #print("True")
                                        #print(dictgenes2[templist[templist.find(",")+1::],int(word)])
                                        #print(len(list(templist.split(","))))
                                        templist+=","+dictgenes2[templist[templist.find(",")+1::],int(word)]
                                        #print(templist)
                                    if len(tempseq1)>1:
                                        dict752[templist[0:-1]]="test"
                                        #if templist not in dictall:
                                        #    print(templist)
                                        #print(templist)
                                        #print(templist)
                                #print(templist)
                                        #print(templist)
                                #print(templist)
                            #print(templist)
                            if count==18:
                                tempword=word
                            if count==6:
                                basepos1=word    
                            if count==28:
                                cov=word
                            if count==65:
                                VF=word
                            if count==67 and word!="":
                                if "->" not in word:
                                    VRF=int(word)
                                else:
                                    VRF=word
                                #rint(VRF)
                            count+=1
                #if "20xxTXxxx0021PfB1290_S20_L001" in lines:
                #        print(templist)
                #if "21USxxxxx0Dd2PfD1290_S12_L001" in lines:
                #    print(templist)
                #if templist[0:templist.find(",")]=="SRR8950984":
                    #print(templist)
                #print(len(templist.split(",")))
                #if "19xxFLxxx0071PfB1230_S20_L001" in templist and "PfMDR1" in templist:
                #    print(templist)
                #print(VRF)
                #if "SRR8950949" in templist:
                #    print(templist)
                if VRF!="" and int(str(VRF)[0])>1:
                    #print(VRF)
                    if templist in wholegenilist1 and int(str(VRF)[0])>1:
                        wholegenilistcut1+=[templist[0:-1]+"#"]
                        wholetypelist1[templist[0:-1]+"#"]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                        wholegenilist1+=[templist+"#"]
                        wholecovlist1[templist[0:-1]+"#"]=cov
                        wholevaflist1[templist[0:-1]+"#"]=VF
                        wholebplist1[templist[0:-1]+"#"]=basepos1
                        wholetypelist1f[templist+"#"]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                        wholecovlist1f[templist+"#"]=cov
                        wholevaflist1f[templist+"#"]=VF
                        wholebplist1f[templist+"#"]=basepos1
                    #if templist in wholegenilist1
                    if tempword!="" and len(templist.split(","))>2 and templist not in wholegenilist1:
                        #print(templist)
                        #print(templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::])
                        if tempword[0:2]=="MN" and tempword[-2::]=="IE":
                            wholegenilist1+=[templist]
                            wholegenilist1+=[templist2]
                            wholegenilistcut1+=[templist[0:-1]]
                            wholegenilistcut1+=[templist2[0:-1]]
                            wholetypelist1[templist[0:-1]]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                            wholecovlist1[templist[0:-1]]=cov
                            wholevaflist1[templist[0:-1]]=VF
                            wholebplist1[templist[0:-1]]=basepos1
                            wholetypelist1f[templist]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                            wholecovlist1f[templist]=cov
                            wholevaflist1f[templist]=VF
                            wholebplist1f[templist]=basepos1
                        else:
                            wholegenilistcut1+=[templist[0:-1]]
                            wholetypelist1[templist[0:-1]]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                            wholegenilist1+=[templist]
                            wholecovlist1[templist[0:-1]]=cov
                            wholevaflist1[templist[0:-1]]=VF
                            wholebplist1[templist[0:-1]]=basepos1
                            wholetypelist1f[templist]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                            wholecovlist1f[templist]=cov
                            wholevaflist1f[templist]=VF
                            wholebplist1f[templist]=basepos1


#print(dictvar)
#print(wholetypelist1)


for files in wholefiles:
    with open(files,"r") as f1:
        #print(files)
        count=0
        countcom1=0
        countcom2=0
        if files!="geneiousannotationdomall4/.DS_Store":
            for lines in f1:
                count=0
                current=""
                templist=""
                tempword=""
                templist2=""
                VF=""
                cov=""
                basepos1=""
                samplename=""
                samplegene=""
                #VRF=""
                if lines.find("Coverage:")!=-1 and lines.find("Coverage - High")!=-1:
                    for word in lines.split(","):
                        if count==0:
                            for word2 in word.split(" "):
                                #print(word2[0:-6])
                                #print(word2)
                                templist+=word2
                                samplename=word2
                                #print(templist)
                                break
                        if count==1:
                            #print(word)
                            templist+=","
                            if word=="mitochondrial genome - CYTB CDS":
                                templist+="CYTOb"
                                samplegene="CYTOb"
                            if word=="DHPS_437Corrected ":
                                templist+="DHPS"
                                samplegene="DHPS"
                            if word=="PfMDR1 ":
                                templist+="PfMDR1"
                                samplegene="PfMDR1"
                            if word!="mitochondrial genome - CYTB CDS" and word!="DHPS_437Corrected " and word!="PfMDR1 ":
                                templist+=word
                                samplegene=word
                        #print(templist)
                        if count==57:
                            #print(templist)
                            #print(templist)
                            #print(templist[templist.find(",")+1::])
                            #print(word)
                            #print(word[:-1]+word[0])
                            str1=samplename+","+samplegene+","+word 
                            #print(str1[0:-1])
                            #if samplename=="20CDNVxxx0003PfB1290_S3_L001":
                            #    print(str1)
                            #    print(str1[0:-1])
                            #    print(str1[0:-1] in dictvarbegin)
                            #print(str1)
                            if str1[0:-1] in dictvar:
                                #print("true")
                                #print(dictvarbegin[str1[0:-1]][0])
                                #print(dictvarend[str1[0:-1]])
                                if dictvarbegin[str1[0:-1]][0]!=dictvarend[str1[0:-1]]:
                                    #print("True")
                                    templist=""
                                #else:templist+=","+word[:-1]+word[0]
                            else:
                                templist+=","+word[:-1]+word[0]
                            #if "18xxIL00x0079PfB1190_S75_L001" in lines:
                                #str1=samplename+","+samplegene+","+word
                                #if str1 in dictvar:
                                    #print(lines)
                                #if word in dict1:
                                #    print(templist,word)
                        #print(templist)
                        if count==6:
                            basepos1=word    
                        if count==36:
                            cov=word
                        if count==61:
                            VF="NA"
                        count+=1
                #print(templist)
                #if templist[0:templist.find(",")]=="SRR8950984":
                if templist!="":
                    #print(templist)
                    #print(templist in dict1)
                    if templist in wholegenilist1:
                        wholegenilistcut1+=[templist[0:-1]+"#"]
                        wholetypelist1[templist[0:-1]+"#"]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                        wholegenilist1+=[templist+"#"]
                        wholecovlist1[templist[0:-1]+"#"]=cov
                        wholevaflist1[templist[0:-1]+"#"]=VF
                        wholebplist1[templist[0:-1]+"#"]=basepos1
                        wholetypelist1f[templist+"#"]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                        wholecovlist1f[templist+"#"]=cov
                        wholevaflist1f[templist+"#"]=VF
                        wholebplist1f[templist+"#"]=basepos1
                    if templist not in wholegenilist1:
                        if tempword[0:2]=="MN" and tempword[-2::]=="IE":
                            wholegenilist1+=[templist]
                            wholegenilist1+=[templist2]
                            wholegenilistcut1+=[templist[0:-1]]
                            wholegenilistcut1+=[templist2[0:-1]]
                            wholecovlist1[templist[0:-1]]=cov
                            wholevaflist1[templist[0:-1]]=VF
                            wholebplist1[templist[0:-1]]=basepos1
                            wholetypelist1[templist[0:-1]]="WT"
                            wholetypelist1f[templist]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                            wholecovlist1f[templist]=cov
                            wholevaflist1f[templist]=VF
                            wholebplist1f[templist]=basepos1
                        else:
                            #print(templist)
                            wholegenilistcut1+=[templist[0:-1]]
                            wholegenilist1+=[templist]
                            wholecovlist1[templist[0:-1]]=cov
                            wholevaflist1[templist[0:-1]]=VF
                            wholebplist1[templist[0:-1]]=basepos1
                            wholetypelist1[templist[0:-1]]="WT"
                            wholetypelist1f[templist]=templist[templist.find(",")+1+templist[templist.find(",")+1::].find(",")+1::]
                            wholecovlist1f[templist]=cov
                            wholevaflist1f[templist]=VF
                            wholebplist1f[templist]=basepos1



#print(wholegenilist1)

#print(wholegenilist1)
wholecount=0
#print(wholegenilist1)
#wholecombinedlist1=wholelist1
wholecombinedlist1=[]
for item in wholelist1:
    if item not in wholecombinedlist1:
        wholecombinedlist1+=[item]

for item in wholegenilist1:
    if item not in wholecombinedlist1:
        wholecombinedlist1+=[item]

#for item in wholelist1:
#    if item not in wholegenilist1:
#        print(item)

for item in wholecombinedlist1:
    #print(item)
    #print(item)
    #if item in wholetypelist1 and wholetypelist1[item]=="WT":
    #    if item in dict1:
    #        print(item)
    #print(item)
    #if item[0:-1] not in wholegenilistcut1 and item[0:-1] not in dictall:
    #    print(item)
    #if "20xxTXxxx0021PfB1290_S20_L001" in item:
    #    print(item)
    #if "20xxTXxxx0021PfB1290_S20_L001" in item:
    #    if wholetypelist1[item[0:-1]]=="K76N":
    #        print(item)
    #if "SRR8950949,DHPS,S436A" in item:
    #    print(item)
    #    print(item in wholegenilist1)
    #    print(item in dictall2)
    #    print(item[0:-1] in wholegenilistcut1)
    #    print(item[0:-1] in dictall)
    if "#" in item:
        dict1[item]=item[0:-1]+",NA"+","+wholetypelist1f[item]
        dict4[item]=item[0:-1]+",NA"+","+wholebplist1f[item]
        dict2[item]=item[0:-1]+",NA"+","+wholecovlist1f[item]
        dict3[item]=item[0:-1]+",NA"+","+wholevaflist1f[item]
    else:
        if item in dictall2 and item in wholegenilist1:
            #print("True")
            dict1[item[0:-1]]=dict1[item[0:-1]]+","+wholetypelist1[item[0:-1]]
            dict4[item[0:-1]]=dict4[item[0:-1]]+","+wholebplist1[item[0:-1]]
            dict2[item[0:-1]]=dict2[item[0:-1]]+","+wholecovlist1[item[0:-1]]
            dict3[item[0:-1]]=dict3[item[0:-1]]+","+wholevaflist1[item[0:-1]]
        if item in dictall2 and item not in wholegenilist1 and item[0:-1] in dictall and item[0:-1] in wholegenilistcut1:
            #print("true")
            #print(item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
            #print(dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
            #print(dict1[item])
            #print(wholetypelist1[item])
            #if "SRR8950949,DHPS,S436" in item:
            #    print(item)
            #    print(item in wholegenilist1)
            #    print(item in dictall2)
            #    print(item[0:-1] in wholegenilistcut1)
            #    print(item[0:-1] in dictall)
            dict1[item]=dict1f[item]+","+"NA"
            dict4[item]=dict4f[item]+","+"NA"
            dict2[item]=dict2f[item]+","+"NA"
            dict3[item]=dict3f[item]+","+"NA"
            #if "SRR8950949,DHPS,S436" in item:
            #    print(item)
            #    print(dict1[item])
            #    print(dict2[item])
            #    print(dict3[item])
            #    print(dict4[item])
            #if "SRR8950949,DHPS,S436G" in item:
            #    print("Found it")
            #    print(item)
            #    print(dict1[item])
            #    print(dict2[item])
            #    print(dict3[item])
            #    print(dict4[item])
            #if "SRR8950949,DHPS,S436G" in item:
            #    print(dict1[item])
            #    print(dict2[item])
            #    print(dict3[item])
            #    print(dict4[item])
                #print(dict1[item])
            #print("True")
            #dict1[item]=dict1[item]+",NA"
        if item not in dictall2 and item in wholegenilist1 and item[0:-1] in dictall and item[0:-1] in wholegenilistcut1:
            #print("true")
            #if "SRR8950949,DHPS,S436A" in item:
            #    print("Found it")
            #print(item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
            #print(dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
            #print(dict1[item])
            #print(wholetypelist1[item])
            #if "SRR8950949,DHPS,S436A" in item:
            #    print(wholetypelist1f[item])
            #    print(wholebplist1f[item])
            #    print(wholecovlist1f[item])
            #    print(wholevaflist1f[item])
            dict1[item]=item+",NA"+","+wholetypelist1f[item]
            dict4[item]=item+",NA"+","+wholebplist1f[item]
            dict2[item]=item+",NA"+","+wholecovlist1f[item]
            dict3[item]=item+",NA"+","+wholevaflist1f[item]
        if item[0:-1] in dictall and item[0:-1] not in wholegenilistcut1:
            #if "S533C" in item:
            #print(item in wholegenilist1)
            dict1[item[0:-1]]=dict1[item[0:-1]]+","+"NA"
            dict4[item[0:-1]]=dict4[item[0:-1]]+","+"NA"
            dict2[item[0:-1]]=dict2[item[0:-1]]+","+"NA"
            dict3[item[0:-1]]=dict3[item[0:-1]]+","+"NA"

        if item[0:-1] not in dictall and item[0:-1] in wholegenilistcut1:
            #print(item)
            dict1[item[0:-1]]=item+",NA"+","+wholetypelist1[item[0:-1]]
            dict4[item[0:-1]]=item+",NA"+","+wholebplist1[item[0:-1]]
            dict2[item[0:-1]]=item+",NA"+","+wholecovlist1[item[0:-1]]
            dict3[item[0:-1]]=item+",NA"+","+wholevaflist1[item[0:-1]]
        #print(dict1[item])
    #if "19xxFLxxx0071PfB1230_S20_L001" in item and item in dict1:
    #    print(dict1[item])
    #if "19xxFLxxx0071PfB1230_S20_L001" in item and item[0:-1] in dict1:
    #    print(dict1[item[0:-1]])
    #wholecount+=1
#for item in dict1:
#    if item not in wholecombinedlist1:

#print(dict1["SRR8950949,DHPS,S436G"])
#print(dict1["SRR8950949,DHPS,S436A"])
#print(dict2["SRR8950949,DHPS,S436A"])
#print(dict3["SRR8950949,DHPS,S436A"])
#print(dict4["SRR8950949,DHPS,S436A"])
#print(dict1)
#print(dict1)
#for item in dict751:
#    if item not in dictall:
#        print(item)

#for item in dict752:
#    if item not in dictall:
#        print(item)


with open("testdomsamfixbp19.csv", 'w') as t1:
    t1.write("Sample,Gene,SNP,NFNeST,Geneious"+"\n")
    for item in dict1:
        #print(item)
        if item=="Dd2,PfMDR1,N86Y":
                t1.write(item+dict1[item][:-5]+",N86F"+"\n")
        #print(item)
        #print(item[item.find(",")+1::].find(","))
        #print(item[item.find(",")+1:item.find(",")+item[item.find(",")+1::].find(",")])
        #print(item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::])
        #if item in wholetypelist1:
        #    if dict1[item]==item+",NA"+","+wholetypelist1[item]:
        #        print(dict1[item])
        #print(dict1[item])
        #print(dict1[item][-1])
        #if dict1[item][-1].isdigit():
        #print(dict1[item])
        #if "N75E" in item:
        #    print(dict1[item])
        #if len(list(dict1[item].split(",")))>5:
        #    print(dict1[item])
        #if item in dict751======
        #\if len(list(dict1[item].split(",")))==6:
        #    print(dict1[item])
        #if "20xxTXxxx0021PfB1290_S20_L001" in item:
        #    print(dict1[item])
        #if "SRR8950949,DHPS,S436G" in item:
        #    print(item in dict751)
        #    print(item in dict752)
        #    print(dict1[item])
        #print(item)
        if item[-1].isdigit()==True:
            #if "SRR8950949" in item:
                #print(item)
                #print(dict1[item])
                #print(item in dict751)
                #print(item in dict752)
                #print(item in dict751)
                #print(item in dict752)
                #print(dict1[item])
            #if "SRR8950949,DHPS,S436" in item:
            #    print(item in dict751)
            #    print(item in dict752)
            if item in dict751 and item in dict752:
                #t1.write(dict1[item]+"\n")
                #print(dict1[item])
                #print(dict4[item])
                #if "20xxTXxxx0021PfB1290_S20_L001" in dict1[item]:
                #print(dict1[item])
                #print(dict2[item])
                if "N75E,N75E" in dict1[item]:
                    if len(list(dict1[item].split(",")))>5:
                        t1.write(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1]+"\n")
                    else: t1.write(dict1[item]+"\n")
                    t1.write(item[0:item.find(",")]+",basepos,"+list(dict1[item].split(","))[2]+","+"495,495"+"\n")
                    if len(list(dict2[item].split(",")))>2:
                        t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+list(dict2[item].split(","))[1]+","+list(dict2[item].split(","))[2]+"\n")
                    if len(list(dict3[item].split(",")))>2:
                        t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+list(dict3[item].split(","))[1]+","+list(dict3[item].split(","))[2]+"\n")
                    if len(list(dict3[item].split(",")))==2:
                        t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+dict2[item]+"\n")
                    if len(list(dict3[item].split(",")))==2:
                        t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+dict3[item]+"\n")
                    if len(list(dict1[item].split(",")))>5:
                        t1.write(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1]+"\n")
                    else: t1.write(dict1[item]+"\n")
                    t1.write(item[0:item.find(",")]+",basepos,"+list(dict1[item].split(","))[2]+","+"497,497"+"\n")
                    if len(list(dict2[item].split(",")))>2:
                        t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+list(dict2[item].split(","))[1]+","+list(dict2[item].split(","))[2]+"\n")
                    if len(list(dict3[item].split(",")))>2:
                        t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+list(dict3[item].split(","))[1]+","+list(dict3[item].split(","))[2]+"\n")
                    if len(list(dict3[item].split(",")))==2:
                        t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+dict2[item]+"\n")
                    if len(list(dict3[item].split(",")))==2:
                        t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+dict3[item]+"\n")
                #else:
                #    print(item)
            if item not in dict751 and item in dict752:
            #    print(dict1[item])
                #if len(list(dict1[item].split(",")))<5:
                #    print("Geneious)")
                #    print(item)
                #print(dict1[item])
                if len(list(dict1[item].split(",")))>5:
                    t1.write(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1]+"\n")
                    t1.write(item[0:item.find(",")]+",basepos,"+list(dict1[item].split(","))[2]+","+list(dict4[item].split(","))[0]+","+list(dict4[item].split(","))[1]+"\n")
                    t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+list(dict2[item].split(","))[0]+","+list(dict2[item].split(","))[1]+"\n")
                    t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+list(dict3[item].split(","))[0]+","+list(dict3[item].split(","))[1]+"\n")
                else:
                    t1.write(dict1[item]+"\n")
                    t1.write(item[0:item.find(",")]+",basepos,"+list(dict1[item].split(","))[2]+","+dict4[item]+"\n")
                    t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+dict2[item]+"\n")
                    t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+dict3[item]+"\n")
            if item in dict751 and item not in dict752:
                #if "SRR8950949" in item:
                #    print(item)
                #    print(dict1[item])
                #    print(dict2[item])
                #    print(dict3[item])
                #    print(dict4[item])
                #print(dict1[item])
                if len(list(dict1[item].split(",")))<5:
                    continue
                else:
                    t1.write(dict1[item]+"\n")
                    t1.write(item[0:item.find(",")]+",basepos,"+list(dict1[item].split(","))[2]+","+dict4[item]+"\n")
                    t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+dict2[item]+"\n")
                    t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+dict3[item]+"\n")
            #if len(list(dict1[item].split(",")))==7 and item not in dict751 and item not in dict752:
                #print(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1])
                #print(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1])
            #    print(dict1[item][0:-len(list(dict1[item].split(",")[-2]))-1])
            #    print(list(dict1[item].split(","))[2]+","+list(dict4[item].split(","))[0]+","+list(dict4[item].split(","))[1])
            #    t1.write(dict1[item][0:-len(list(dict1[item].split(",")[-2]))-1]+"\n")
            #    t1.write(item[0:item.find(",")]+",basepos,"+list(dict1[item].split(","))[2]+","+list(dict4[item].split(","))[0]+","+list(dict4[item].split(","))[1]+"\n")
            #    t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+list(dict2[item].split(","))[0]+","+list(dict2[item].split(","))[1]+"\n")
            #    t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+list(dict3[item].split(","))[0]+","+list(dict3[item].split(","))[1]+"\n")
            if len(list(dict1[item].split(",")))>5 and item not in dict751 and item not in dict752:
                #print(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1])
                #print(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1])
                #if len(list(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1].split(",")))>5:
                #    print(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1])
                #print(len(list(dict1[item].split(","))))
                t1.write(dict1[item][0:-len(list(dict1[item].split(",")[-1]))-1]+"\n")
                t1.write(item[0:item.find(",")]+",basepos,"+list(dict1[item].split(","))[2]+","+list(dict4[item].split(","))[0]+","+list(dict4[item].split(","))[1]+"\n")
                t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+list(dict2[item].split(","))[0]+","+list(dict2[item].split(","))[1]+"\n")
                t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+list(dict3[item].split(","))[0]+","+list(dict3[item].split(","))[1]+"\n")
            if len(list(dict1[item].split(",")))<=5 and item not in dict751 and item not in dict752:
                #if len(list(dict1[item].split(",")))==
                #if "SRR8950949,DHPS,S436G" in item:
                #    print(dict1[item])
        #    print(item in dict751)
        #    print(item in dict752)
        #    print(dict1[item])
                t1.write(dict1[item]+"\n")
                #print(dict4[item])
                if len(list(dict4[item].split(",")))>2:
                    t1.write(item[0:item.find(",")]+",basepos,"+list(dict1[item].split(","))[2]+","+list(dict4[item].split(","))[-2]+","+list(dict4[item].split(","))[-1]+"\n")
                if len(list(dict2[item].split(",")))>2:
                    t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+list(dict2[item].split(","))[-2]+","+list(dict2[item].split(","))[-1]+"\n")
                if len(list(dict3[item].split(",")))>2:
                    t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+list(dict3[item].split(","))[-2]+","+list(dict3[item].split(","))[-1]+"\n")
                if len(list(dict4[item].split(",")))==2:
                    t1.write(item[0:item.find(",")]+",basepos,"+list(dict1[item].split(","))[2]+","+dict4[item]+"\n")
                if len(list(dict2[item].split(",")))==2:
                    t1.write(item[0:item.find(",")]+",coverage,"+list(dict1[item].split(","))[2]+","+dict2[item]+"\n")
                if len(list(dict3[item].split(",")))==2:
                    t1.write(item[0:item.find(",")]+",Variant frequency,"+list(dict1[item].split(","))[2]+","+dict3[item]+"\n")
        if item[-1].isdigit()==False:
            #print(item) 
            t1.write(dict1[item]+"\n")
            t1.write(dict2[item]+"\n")
            t1.write(dict3[item]+"\n")
            t1.write(dict4[item]+"\n")
            #print(dict2[item])
            #print(dict3[item])
            #print(dict4[item])
        #    if "19xxFLxxx0071PfB1230_S20_L001" in item:
        #        print(dict1[item])

#reader = csv.reader(open("testdomsamfix4.csv"), delimiter=";")
#sortedlist = sorted(reader, key=operator.itemgetter(3), reverse=True)
#print(sortedlist)

#with open("testdomsamfixbp17.csv", 'r') as t1:
#    for lines in t1:
#        if len(list(lines.split(",")))>5:
#            print(lines)
            #print(len(list(lines.split(","))))