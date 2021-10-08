import operator

with open("testdomsamfixbp22ny.csv", 'r') as t1:
    for lines in t1:
        if len(list(lines.split(",")))>5:
            #print(len(list(lines.split(","))))
            print(lines)
            #print(len(list(lines.split(","))))

dict1={}
with open("testdomsamfixbp22ny.csv", "r") as r1:
    with open("discrepancytestdomsamfixbp170ny.csv", "w") as r2:
        #r2.write("Sample,Gene,SNP,NFNeST,Geneious"+"\n")
        #print(r2)
        count=0
        for line in r1:
            if count==0:
                r2.write(line.strip("\n")+",Difference,Flag"+"\n")
            else:
            #print(lines)
            #print(lines[lines.find(",")+1::])
            #print(lines[lines.find(",")+1+lines[lines.find(",")+1::].find(",")+1::])
            #print(lines[-8::])
            #abc=lines[-8::]
            #print(abc[abc.find(",")+1::])
            #print(abc[abc.find(",")+1:abc.find(",")+1+abc[abc.find(",")+1::].find(",")])
            #print(abc[abc.find(",")+1:abc.find(",")+1+abc[abc.find(",")+1::].find(",")])
            #print(abc[abc.find(",")+2+abc[abc.find(",")+1::].find(",")::])
            #print((abc[abc.find(",")+1:abc.find(",")+1+abc[abc.find(",")+1::].find(",")]))
            #print((abc[abc.find(",")+2+abc[abc.find(",")+1::].find(",")::]))
            #if abc[abc.find(",")+1:abc.find(",")+1+abc[abc.find(",")+1::].find(",")]==abc[abc.find(",")+2+abc[abc.find(",")+1::].find(",")::]:
            #    print("yes")
            #if abc[abc.find(",")+1:abc.find(",")+1+abc[abc.find(",")+1::].find(",")]!=abc[abc.find(",")+2+abc[abc.find(",")+1::].find(",")::]:
                #print(lines)
            #    r2.write(lines)
            #print(lines)
            #if abc[abc.find(",")+2+abc[abc.find(",")+1::].find(",")::]!=abc[abc.find(",")+1:abc.find(",")+1+abc[abc.find(",")+1::].find(",")]+"\n":
            #    r2.write(lines)
            #if lines[-1]!="\n":
            #    lines=lines+"\n"
            #print(lines)
            #print(lines[lines.find(",")+1+lines[lines.find(",")+1::].find(",")+1::])
            #print()
            #pos1=lines.find(",")
            #chr1=lines[lines.find(",")+1::]
            #chr2=lines[pos1+chr1.find(",")+2::]
            #print(list(line.split(",")))
                a=list(line.split(","))
                #if len(a)<5:
                #    print(line)
                #print(line)
                #print(a)
                if len(a)<6 and a[1]=="coverage" and "->" not in a[4] and "NA" not in a[3] and "NA" not in a[4]:
                    #print(a[-2])
                    #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        #r2.write(line.strip("\n")+","+str(abs(int(a[3])-int(a[4].strip("\n"))))+"\n")
                        dict1[line.strip("\n")+","]=str(abs(int(a[3])-int(a[4].strip("\n"))))
                    #print(chr2)
                if len(a)<6 and a[1]=="Variant frequency" and "->" not in a[4] and "NA" not in a[3] and "NA" not in a[4]:
                    #print(a[-2])
                    #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        #print(a[4][0:-2])
                        #r2.write(line.strip("\n")+","+str(abs(float(a[3][0:-1])-float(a[4][0:-2])))+"%\n")
                        dict1[line.strip("\n")+","]=str(abs(float(a[3][0:-1])-float(a[4][0:-2])))
                    #print(chr2)
                if len(a)<6 and a[1]=="coverage" and "->" in a[4]:
                #print(a[-2])
                #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        r2.write(line.strip("\n")+",,Change\n")
                if len(a)<6 and a[1]=="Variant frequency" and "->" in a[4]:
                #print(a[-2])
                #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        r2.write(line.strip("\n")+",,Change\n")
                if len(a)<6 and a[1]!="Variant frequency" and a[1]!="coverage":
                #print(a[-2])
                #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        r2.write(line.strip("\n")+",,Sample\n")
                if len(a)>=6:
                    #print(a)
                    b=[a[0],a[1],a[2],a[-2],a[-1]]
                    #print(line)
                    #print(b)
                    if b[-2]+"\n"!=b[-1]:
                        my_string = ','.join(b)
                        r2.write(my_string)
            count+=1

#print(dict1)
#dict2 = dict(sorted(dict1.items(), key=lambda t: t[::-1]))
dict2=sorted(dict1, key=lambda i: float(dict1[i]))
with open("discrepancytestdomsamfixbp170ny.csv", "a") as r2:
    for x in range(len(dict2)):
        #print(dict2[x]+","+dict1[dict2[x]]+"\n")
        if float(dict1[dict2[x]])<=1:
            if "Variant frequency" in dict2[x]:
                r2.write(dict2[x]+dict1[dict2[x]]+"%\n")
            else:
                r2.write(dict2[x]+dict1[dict2[x]]+"\n")
        else:
            if "Variant frequency" in dict2[x]:
                r2.write(dict2[x]+dict1[dict2[x]]+"%,Flag\n")
            else:
                r2.write(dict2[x]+dict1[dict2[x]]+",Flag\n")

count=0
with open("discrepancytestdomsamfixbp170ny.csv", "r") as f2:
    for line in f2:
        if "V73V" in line:
            count+=1
print(count)


