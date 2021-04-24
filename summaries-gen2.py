import os

wholefiles=[]
for subdir, dirs, files in os.walk("Geneioustables"):
    for file in files:
        wholefiles+=[os.path.join(subdir, file)]

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
                if lines.find("CDS Codon Number")!=-1:
                    pos2=lines.find("CDS Codon Number")+1
                if lines.find("CDS Position")!=-1:
                    pos2=lines.find("CDS Position")+1
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
                            print(files[files.find("/")+1:files.find("_")]+","+item+","+tempword1[1]+tempword2[1::]+tempword1[-1])
                    #print(tempword1[1]+tempword2[1::]+tempword1[-1])
                    #print(tempword2[1::])
                    #print(lines)

