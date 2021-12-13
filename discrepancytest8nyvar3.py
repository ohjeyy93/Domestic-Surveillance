import operator

#with open("testdomsamfixbp22ny.csv", 'r') as t1:
#    for lines in t1:
#        if len(list(lines.split(",")))>5:
            #print(len(list(lines.split(","))))
#            print(lines)
            #print(len(list(lines.split(","))))

dict1={}
with open("testdomsamfixbp24nyfb.csv", "r") as r1:
    with open("discrepancytestdomsamfixbp173nyfb.csv", "w") as r2:
        #r2.write("Sample,Gene,SNP,NFNeST,Geneious"+"\n")
        #print(r2)
        count=0
        testcount=0
        temptestcount=0
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
                #print(a)
                #print(a[-1])
                #print(a[-5])
                if a[1]!="Variant frequency" and a[1]!="coverage" and a[1]!="basepos" and a[7]!="NA\n" and a[7]!="WT\n":
                    #print(a)
                    if a[-5]+"\n"!=a[-1]:
                        r2.write(line)
                        testcount+=1
                if a[1]=="coverage":
                    #print(a[3])
                    #print(a)
                    if testcount!=temptestcount:
                        if a[4]+"\n"!=a[7]:
                            r2.write(line)
                if a[1]=="Variant frequency":
                    #print(a[3])
                    #print(a)
                    #print(a[-5])
                    if testcount!=temptestcount:
                        if a[4]+"\n"!=a[7]:
                            r2.write(line)
                            testcount=temptestcount

            count+=1


count=0
with open("discrepancytestdomsamfixbp173nyfb.csv", "r") as f2:
    for line in f2:
        if "V73V" in line:
            count+=1
print(count)


