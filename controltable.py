import pandas as pd
df = pd.read_csv("Control-SNPs.csv")

list1=[]
with open("semi1.csv", 'w') as t1:
    for x in range(len(df)):
        if df.iloc[x,0]!="Sample":
            if type(df.iloc[x,1])==str:
                count=0
                for y in df.iloc[x,1]:
                    if count==0 and y=="C":
                        print(df.iloc[x,0]+","+"PfCRT"+",C72S,WT")
                    if count==1 and y=="V":
                        print(df.iloc[x,0]+","+"PfCRT"+",V73V,WT")
                    if count==2 and y=="M":
                        print(df.iloc[x,0]+","+"PfCRT"+",M74I,WT")
                    if count==3 and y=="N":
                        print(df.iloc[x,0]+","+"PfCRT"+",N75E,WT")
                    if count==4 and y=="K":
                        print(df.iloc[x,0]+","+"PfCRT"+",K76T,WT")
                    if count==0 and y=="S":
                        print(df.iloc[x,0]+","+"PfCRT"+",C72S,C72S")
                    if count==2 and y=="I":
                        print(df.iloc[x,0]+","+"PfCRT"+",M74I,M74I")
                    if count==3 and y=="E":
                        print(df.iloc[x,0]+","+"PfCRT"+",N75E,N75E")
                    if count==4 and y=="T":
                        print(df.iloc[x,0]+","+"PfCRT"+",K76T,K76T")
                    count+=1
            else:
                print(df.iloc[x,0]+","+"PfCRT"+",C72S,NA")
                print(df.iloc[x,0]+","+"PfCRT"+",V73V,NA")
                print(df.iloc[x,0]+","+"PfCRT"+",M74I,NA")
                print(df.iloc[x,0]+","+"PfCRT"+",N75E,NA")
                print(df.iloc[x,0]+","+"PfCRT"+",K76T,NA")
        for k in range(2,10):
            if type(df.iloc[x,k])==str:
                if k==2 and df.iloc[x,k]=="N":
                    print(df.iloc[x,0]+",PfMDR1,"+"N86Y,WT")
                if k==3 and df.iloc[x,k]=="E":
                    print(df.iloc[x,0]+",PfMDR1,"+"E130K,WT")
                if k==4 and df.iloc[x,k]=="D":
                    print(df.iloc[x,0]+",PfMDR1,"+"D144G,WT")
                if k==5 and df.iloc[x,k]=="Y":
                    print(df.iloc[x,0]+",PfMDR1,"+"Y184F,WT")
                if k==6 and df.iloc[x,k]=="S":
                    print(df.iloc[x,0]+",PfMDR1,"+"S1034C,WT")
                if k==7 and df.iloc[x,k]=="N":
                    print(df.iloc[x,0]+",PfMDR1,"+"N1042D,WT")
                if k==8 and df.iloc[x,k]=="V":
                    print(df.iloc[x,0]+",PfMDR1,"+"V1109V,WT")
                if k==9 and df.iloc[x,k]=="D":
                    print(df.iloc[x,0]+",PfMDR1,"+"D1246Y,WT")
                if k==2 and df.iloc[x,k]=="Y":
                    print(df.iloc[x,0]+",PfMDR1,"+"N86Y,N86Y")
                if k==2 and df.iloc[x,k]=="Y/F":
                    print(df.iloc[x,0]+",PfMDR1,"+"N86Y,N86Y")
                    print(df.iloc[x,0]+",PfMDR1,"+"N86Y,N86F")
                if k==5 and df.iloc[x,k]=="F":
                    print(df.iloc[x,0]+",PfMDR1,"+"Y184F,Y184F")
                if k==6 and df.iloc[x,k]=="C":
                    print(df.iloc[x,0]+",PfMDR1,"+"S1034C,S1034C")
                if k==7 and df.iloc[x,k]=="D":
                    print(df.iloc[x,0]+",PfMDR1,"+"N1042D,N1042D")
                if k==9 and df.iloc[x,k]=="Y":
                    print(df.iloc[x,0]+",PfMDR1,"+"D1246Y,WT")
            else:
                if k==2:
                    print(df.iloc[x,0]+",PfMDR1,"+"N86Y,NA")
                if k==3:
                    print(df.iloc[x,0]+",PfMDR1,"+"E130K,NA")
                if k==4:
                    print(df.iloc[x,0]+",PfMDR1,"+"D144G,NA")
                if k==5:
                    print(df.iloc[x,0]+",PfMDR1,"+"Y184F,NA")
                if k==6:
                    print(df.iloc[x,0]+",PfMDR1,"+"S1034C,NA")
                if k==7:
                    print(df.iloc[x,0]+",PfMDR1,"+"N1042D,NA")
                if k==8:
                    print(df.iloc[x,0]+",PfMDR1,"+"V1109V,NA")
                if k==9:
                    print(df.iloc[x,0]+",PfMDR1,"+"D1246Y,NA")
                #print(df.iloc[x,0]+",PfMDR1,"+"NA")
                #print(df.iloc[x,0]+","+"PfCRT"+","+df.iloc[x,1])
        for k in range(10,15):
            if type(df.iloc[x,k])==str:
                if k==10 and df.iloc[x,k]=="TGT":
                    print(df.iloc[x,0]+",DHFR,"+"C50R,WT")
                if k==11 and df.iloc[x,k]=="AAT":
                    print(df.iloc[x,0]+",DHFR,"+"N51I,WT")
                if k==11 and df.iloc[x,k]=="ATT":
                    print(df.iloc[x,0]+",DHFR,"+"N51I,N51I")
                if k==12 and df.iloc[x,k]=="TGT":
                    print(df.iloc[x,0]+",DHFR,"+"C59R,WT")
                if k==12 and df.iloc[x,k]=="CGT":
                    print(df.iloc[x,0]+",DHFR,"+"C59R,C59R")
                if k==13 and df.iloc[x,k]=="AGC":
                    print(df.iloc[x,0]+",DHFR,"+"S108N,WT")
                if k==13 and df.iloc[x,k]=="AAC":
                    print(df.iloc[x,0]+",DHFR,"+"S108N,S108N")
                if k==13 and df.iloc[x,k]=="ACC":
                    print(df.iloc[x,0]+",DHFR,"+"S108N,S108T")
                if k==14 and df.iloc[x,k]=="ATA":
                    print(df.iloc[x,0]+",DHFR,"+"I164L,WT")
                if k==14 and df.iloc[x,k]=="TTA":
                    print(df.iloc[x,0]+",DHFR,"+"I164L,I164L")

        for k in range(15,20):
            if type(df.iloc[x,k])==str:
                if k==15 and df.iloc[x,k]=="TCT":
                    print(df.iloc[x,0]+",DHPS,"+"S436A,WT")
                if k==15 and df.iloc[x,k]=="TCT":
                    print(df.iloc[x,0]+",DHPS,"+"S436F,WT")
                if k==15 and df.iloc[x,k]=="TTT":
                    print(df.iloc[x,0]+",DHPS,"+"S436F,S436F")
                if k==15 and df.iloc[x,k]=="GCT":
                    print(df.iloc[x,0]+",DHPS,"+"S436A,S436A")
                
                if k==16 and df.iloc[x,k]=="GGT":
                    print(df.iloc[x,0]+",DHPS,"+"G437A,WT")
                if k==16 and df.iloc[x,k]=="GCT":
                    print(df.iloc[x,0]+",DHPS,"+"G437A,G437A")

                if k==17 and df.iloc[x,k]=="AAA":
                    print(df.iloc[x,0]+",DHPS,"+"K540E,WT")

                if k==18 and df.iloc[x,k]=="GCG":
                    print(df.iloc[x,0]+",DHPS,"+"A581G,WT")

                if k==19 and df.iloc[x,k]=="GCC":
                    print(df.iloc[x,0]+",DHPS,"+"A613S,WT")
                if k==19 and df.iloc[x,k]=="GCC":
                    print(df.iloc[x,0]+",DHPS,"+"A613T,WT")
                if k==19 and df.iloc[x,k]=="TCC":
                    print(df.iloc[x,0]+",DHPS,"+"A613S,A613S")
                if k==19 and df.iloc[x,k]=="ACC":
                    print(df.iloc[x,0]+",DHPS,"+"A613T,A613T")



