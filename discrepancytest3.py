with open("testdomsamfixbp16.csv", "r") as r1:
    with open("discrepancytestdomsamfixbp162.csv", "w") as r2:
        #r2.write("Sample,Gene,SNP,NFNeST,Geneious"+"\n")
        #print(r2)
        count=0
        for line in r1:
            if count==0:
                r2.write(line.strip("\n")+",Difference"+"\n")
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
                if len(a)<6 and a[1]=="coverage" and "->" not in a[4] and "NA" not in a[3] and "NA" not in a[4]:
                    #print(a[-2])
                    #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        r2.write(line.strip("\n")+","+str(abs(int(a[3])-int(a[4].strip("\n"))))+"\n")
                    #print(chr2)
                if len(a)<6 and a[1]=="Variant frequency" and "->" not in a[4] and "NA" not in a[3] and "NA" not in a[4]:
                    #print(a[-2])
                    #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        #print(a[4][0:-2])
                        r2.write(line.strip("\n")+","+str(abs(float(a[3][0:-1])-float(a[4][0:-2])))+"%\n")
                    #print(chr2)
                if len(a)<6 and a[1]=="coverage" and "->" in a[4]:
                #print(a[-2])
                #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        r2.write(line)
                if len(a)<6 and a[1]=="Variant frequency" and "->" in a[4]:
                #print(a[-2])
                #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        r2.write(line)
                if len(a)<6 and a[1]!="Variant frequency" and a[1]!="coverage":
                #print(a[-2])
                #print(a[-1])
                    if a[-2]+"\n"!=a[-1]:
                        r2.write(line)
                if len(a)>=6:
                    b=[a[0],a[1],a[2],a[-2],a[-1]]
                    if b[-2]+"\n"!=b[-1]:
                        my_string = ','.join(b)
                        r2.write(my_string)
            count+=1
