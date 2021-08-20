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
                            if item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::][0]==item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::][-1]:
                                dict1[item]=item+",WT"
                            else:
                                dict1[item]=item+","+item[item.find(",")+1+item[item.find(",")+1::].find(",")+1::]
                            #print(dict1[item])
                            dict4[item]=tempbasepos1
                            dict2[item]=tempcov
                            dict3[item]=tempvafdp1 

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
                if lines.find("Polymorphism")!=-1:
                    for word in lines.split(","):
                        if count==0:
                            for word2 in word.split(" "):
                                #print(word2[0:-6])
                                templist+=word2[0:-6]
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
                        wholecovlist1+=[cov]
                        wholevaflist1+=[VF]
                        wholebplist1+=[basepos1]
                    else:
                        wholegenilist1+=[templist]
                        wholecovlist1[templist]=[cov]
                        wholevaflist1[templist]=[VF]
                        wholebplist1[templist]=[basepos1]

#print(wholegenilist1)

#print(wholegenilist1)
wholecount=0
#print(wholegenilist1)
wholecombinedlist1=wholelist1+wholegenilist1
for item in wholecombinedlist1:
    #print(item)
    #print(item)
    if item in wholelist1 and item in wholegenilist1:
        #print("true")
        #print(item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
        #print(dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::])
        dict1[item]=dict1[item]+","+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::]
        dict4[item]=dict4[item]+","+wholebplist1[item]
        dict2[item]=dict2[item]+","+wholecovlist1[item]
        dict3[item]=dict3[item]+","+wholevaflist1[item]
        #print("True")
        #dict1[item]=dict1[item]+",NA"
    if item in wholelist1 and item not in wholegenilist1:
        #if "S533C" in item:
        dict1[item]=dict1[item]+",NA"
        dict4[item]=dict4[item]+","+"NA"
        dict2[item]=dict2[item]+","+"NA"
        dict3[item]=dict3[item]+","+"NA"
    if item not in wholelist1 and item in wholegenilist1:
        dict1[item]=item+"NA"+item[item.find(",")+1+(item[item.find(",")+1::]).find(",")+1::]
        dict4[item]=item+"NA"+wholebplist1[wholecount]
        dict2[item]=item+"NA"+wholecovlist1[wholecount]
        dict3[item]=item+"NA"+wholevaflist1[wholecount]
    #wholecount+=1


#print(dict1)
with open("testdomsam12.csv", 'w') as t1:
    t1.write("Sample,Gene,SNP,NFNeST,Geneious"+"\n")
    for item in dict1:
        #print(item)
        if item=="Dd2,PfMDR1,N86Y":
            t1.write(item+dict1[item][:-5]+",N86F"+"\n")
        print(item)
        t1.write(item+dict1[item]+"\n")
        t1.write(item+","+","+dict4[item]+"\n")
        t1.write(item+","+","+dict2[item]+"\n")
        t1.write(item+","+","+dict3[item]+"\n")

