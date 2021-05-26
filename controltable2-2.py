import pandas as pd
df = pd.read_csv("Control-SNPs.csv")

list1=[]
with open("semi2.csv", 'w') as t1:
    for x in range(len(df)):
        if df.iloc[x,0]!="Sample" and df.iloc[x,0]!="FCR3":
            print(df.iloc[x,0])
            if type(df.iloc[x,1])==str:
                count=0
                for y in df.iloc[x,1]:
                    if count==0 and y=="C":
                        t1.write(df.iloc[x,0]+","+"PfCRT"+",C72S,WT"+"\n")
                    if count==1 and y=="V":
                        t1.write(df.iloc[x,0]+","+"PfCRT"+",V73V,WT"+"\n")
                    if count==2 and y=="M":
                        t1.write(df.iloc[x,0]+","+"PfCRT"+",M74I,WT"+"\n")
                    if count==3 and y=="N":
                        t1.write(df.iloc[x,0]+","+"PfCRT"+",N75E,WT"+"\n")
                    if count==4 and y=="K":
                        t1.write(df.iloc[x,0]+","+"PfCRT"+",K76T,WT"+"\n")
                    if count==0 and y=="S":
                        t1.write(df.iloc[x,0]+","+"PfCRT"+",C72S,C72S"+"\n")
                    if count==2 and y=="I":
                        t1.write(df.iloc[x,0]+","+"PfCRT"+",M74I,M74I"+"\n")
                    if count==3 and y=="E":
                        t1.write(df.iloc[x,0]+","+"PfCRT"+",N75E,N75E"+"\n")
                    if count==4 and y=="T":
                        t1.write(df.iloc[x,0]+","+"PfCRT"+",K76T,K76T"+"\n")
                    count+=1
            else:
                t1.write(df.iloc[x,0]+","+"PfCRT"+",C72S,NA"+"\n")
                t1.write(df.iloc[x,0]+","+"PfCRT"+",V73V,NA"+"\n")
                t1.write(df.iloc[x,0]+","+"PfCRT"+",M74I,NA"+"\n")
                t1.write(df.iloc[x,0]+","+"PfCRT"+",N75E,NA"+"\n")
                t1.write(df.iloc[x,0]+","+"PfCRT"+",K76T,NA"+"\n")
                
            for k in range(2,10):
                if type(df.iloc[x,k])==str:
                    if k==2 and df.iloc[x,k]=="N":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"N86Y,WT"+"\n")
                    if k==3 and df.iloc[x,k]=="E":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"E130K,WT"+"\n")
                    if k==4 and df.iloc[x,k]=="D":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"D144G,WT"+"\n")
                    if k==5 and df.iloc[x,k]=="Y":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"Y184F,WT"+"\n")
                    if k==6 and df.iloc[x,k]=="S":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"S1034C,WT"+"\n")
                    if k==7 and df.iloc[x,k]=="N":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"N1042D,WT"+"\n")
                    if k==8 and df.iloc[x,k]=="V":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"V1109V,WT"+"\n")
                    if k==9 and df.iloc[x,k]=="D":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"D1246Y,WT"+"\n")
                    if k==2 and df.iloc[x,k]=="Y":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"N86Y,N86Y"+"\n")
                    if k==2 and df.iloc[x,k]=="Y/F":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"N86Y,N86Y"+"\n")
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"N86Y,N86F"+"\n")
                    if k==5 and df.iloc[x,k]=="F":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"Y184F,Y184F"+"\n")
                    if k==6 and df.iloc[x,k]=="C":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"S1034C,S1034C"+"\n")
                    if k==7 and df.iloc[x,k]=="D":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"N1042D,N1042D"+"\n")
                    if k==9 and df.iloc[x,k]=="Y":
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"D1246Y,WT"+"\n")
                else:
                    if k==2:
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"N86Y,NA"+"\n")
                    if k==3:
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"E130K,NA"+"\n")
                    if k==4:
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"D144G,NA"+"\n")
                    if k==5:
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"Y184F,NA"+"\n")
                    if k==6:
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"S1034C,NA"+"\n")
                    if k==7:
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"N1042D,NA"+"\n")
                    if k==8:
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"V1109V,NA"+"\n")
                    if k==9:
                        t1.write(df.iloc[x,0]+",PfMDR1,"+"D1246Y,NA"+"\n")
                    #t1.write(df.iloc[x,0]+",PfMDR1,"+"NA")
                    #t1.write(df.iloc[x,0]+","+"PfCRT"+","+df.iloc[x,1])
            for k in range(10,15):
                if type(df.iloc[x,k])==str:
                    if k==10 and df.iloc[x,k]=="TGT":
                        t1.write(df.iloc[x,0]+",DHFR,"+"C50R,WT"+"\n")
                    if k==11 and df.iloc[x,k]=="AAT":
                        t1.write(df.iloc[x,0]+",DHFR,"+"N51I,WT"+"\n")
                    if k==11 and df.iloc[x,k]=="ATT":
                        t1.write(df.iloc[x,0]+",DHFR,"+"N51I,N51I"+"\n")
                    if k==12 and df.iloc[x,k]=="TGT":
                        t1.write(df.iloc[x,0]+",DHFR,"+"C59R,WT"+"\n")
                    if k==12 and df.iloc[x,k]=="CGT":
                        t1.write(df.iloc[x,0]+",DHFR,"+"C59R,C59R"+"\n")
                    if k==13 and df.iloc[x,k]=="AGC":
                        t1.write(df.iloc[x,0]+",DHFR,"+"S108N,WT"+"\n")
                    if k==13 and df.iloc[x,k]=="AAC":
                        t1.write(df.iloc[x,0]+",DHFR,"+"S108N,S108N"+"\n")
                    if k==13 and df.iloc[x,k]=="ACC":
                        t1.write(df.iloc[x,0]+",DHFR,"+"S108N,S108T"+"\n")
                    if k==14 and df.iloc[x,k]=="ATA":
                        t1.write(df.iloc[x,0]+",DHFR,"+"I164L,WT"+"\n")
                    if k==14 and df.iloc[x,k]=="TTA":
                        t1.write(df.iloc[x,0]+",DHFR,"+"I164L,I164L"+"\n")

            for k in range(15,20):
                if type(df.iloc[x,k])==str:
                    if k==15 and df.iloc[x,k]=="TCT":
                        t1.write(df.iloc[x,0]+",DHPS,"+"S436A,WT"+"\n")
                    if k==15 and df.iloc[x,k]=="TCT":
                        t1.write(df.iloc[x,0]+",DHPS,"+"S436F,WT"+"\n")
                    if k==15 and df.iloc[x,k]=="TTT":
                        t1.write(df.iloc[x,0]+",DHPS,"+"S436F,S436F"+"\n")
                    if k==15 and df.iloc[x,k]=="GCT":
                        t1.write(df.iloc[x,0]+",DHPS,"+"S436A,S436A"+"\n")
                    
                    if k==16 and df.iloc[x,k]=="GGT":
                        t1.write(df.iloc[x,0]+",DHPS,"+"G437A,WT"+"\n")
                    if k==16 and df.iloc[x,k]=="GCT":
                        t1.write(df.iloc[x,0]+",DHPS,"+"G437A,G437A"+"\n")

                    if k==17 and df.iloc[x,k]=="AAA":
                        t1.write(df.iloc[x,0]+",DHPS,"+"K540E,WT"+"\n")

                    if k==18 and df.iloc[x,k]=="GCG":
                        t1.write(df.iloc[x,0]+",DHPS,"+"A581G,WT"+"\n")

                    if k==19 and df.iloc[x,k]=="GCC":
                        t1.write(df.iloc[x,0]+",DHPS,"+"A613S,WT"+"\n")
                    if k==19 and df.iloc[x,k]=="GCC":
                        t1.write(df.iloc[x,0]+",DHPS,"+"A613T,WT"+"\n")
                    if k==19 and df.iloc[x,k]=="TCC":
                        t1.write(df.iloc[x,0]+",DHPS,"+"A613S,A613S"+"\n")
                    if k==19 and df.iloc[x,k]=="ACC":
                        t1.write(df.iloc[x,0]+",DHPS,"+"A613T,A613T"+"\n")



