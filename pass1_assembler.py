import os
LC=0
mnemonics={
    'ADD':('IS','01',2),
    'SUB': ('IS','02',2),
    'MOVER':('IS','04',2),
    'MOVEM':('IS','05',2),
    'DS':('DL','01',1),
    'DC':('DL','02',1),
    'START':('AD','01'),
    'END':('AD','02'),
    'ORIGIN':('AD','03'),
    'EQU':('AD','04'),
    'LTORG':('AD','05')
}

REG={
    'AREG':'01',
    'BREG':'02',
    'CREG':'03',
    'DREG':'04'
}

symboltab={}
words=[]
symindex=0
pooltable=[]
file=open("input.txt")
lit=open('literals.txt','a+')
ipf=open("output.txt",'a')
sym=open("symbol.txt",'a+')
temp=open("temp.txt",'a+')
lit.truncate(0)
ipf.truncate(0)
temp.truncate(0)

def littab():
    print("literal table:")
    lit.seek(0,0)
    for x in lit:
        print(x)

#prints pool table
def pooltab2():
    global pooltab
    print("Pool Table:")
    print(pooltab)

#prints symbol table
def symbol():
    global symtab
    print("Symbol Table:")
    print(symboltab)

def start(k):
    global words
    global ipf
    global LC
    if(len(words)>1):
        LC=int(words[k+1])
    else:
        LC+=1
    ipf.write("(AD,01)\t(C,"+str(LC)+")\n")

def end(k):
    global ipf
    global LC
    global lit
    global words
    ipf.write("(AD,02)\n")
    lit.seek(0,0)
    temp.truncate(0)
    for x in lit:
        if "**" in x:
            list1=x.split()
            temp.write(list1[0]+"\t"+str(LC)+"\n")
            LC+=1
        else:
            temp.write(x)
    temp.seek(0,0)     
    lit.truncate(0)
    for i in temp:
        lit.write(i)
    temp.truncate(0)

def ltorg():
    global ipf
    global LC
    global lit
    global words
    lit.seek(0,0)
    temp.truncate(0)
    ipf.write('(AD,05)\n')
    for y in lit:
        if "**" in y:
            x=y.split()
            print("value of x",x)
            LC+=1
            temp.write(x[0]+"\t"+str(LC)+"\n")
            ipf.write(str(LC)+"\t(DL,02)(C,"+str(x[0])+")\n")  
        else:
            temp.write(x)

    lit.truncate(0)
    temp.seek(0,0)
    for i in temp:
        print("writting in literals",i)
        lit.write(i)
    

def ds(k):
    global ipf
    global LC
    global lit
    global words
    a=str(words[k+1])
    ipf.write("(DL,01)(C,"+a+")\n")
    LC+=int(a)

def dc(k):
    global ipf
    global LC
    global lit
    global words
    a=str(words[k+1])
    ipf.write("(DL,01)(C,"+a+")\n")
    LC+=int(a)

def others(mnemonic,k):
    global ipf
    global LC
    global lit
    global words
    global symindex
    LC+=1
    l=mnemonics[mnemonic]
    ipf.write("("+l[0]+","+l[1]+")\t")

    y=l[-1]
    for i in range(1,y+1):
        
        if "=" in words[k+i]:
            lit.seek(0,2)
            lit.write(words[k+i]+"\t**\n")
            lit.seek(0,0)
            x=len(lit.readlines())
            ipf.write("(L,"+str(x)+")\n")


        elif words[k+i] in REG.keys():
            ipf.write("(REG"+","+REG[words[k+i]]+")\t")

        else:
            if words[k+i] in symboltab.keys():
                w=symboltab[words[k+i]]
                ipf.write("(S"+","+str(w[-1])+")\n")
            else:
                symboltab[words[k+i]]=("**",symindex)
                
                ipf.write("(S"+","+str(symindex)+")\n")
                symindex+=1


def deteckmn(k):
    global LC
    global symboltab
    global symindex
    if (words[k]=='START'):
        start(k)
    elif(words[k]=='END'):
        end(k)
    elif(words[k]=='LTORG'):
        ltorg()
    elif(words[k]=='DC'):
        print(LC)
        ipf.write(str(LC)+"\t")
        dc(k)
    elif(words[k]=='DS'):
        ipf.write(str(LC)+"\t")
        ds(k)
    else:
        ipf.write(str(LC)+"\t")
        others(words[k],k)



for line in file:
    
    words=line.split()
    print(words)
    if words[0]  in mnemonics.keys():
        k=0
        deteckmn(k)

    else:
        k=1
        symboltab[words[0]]=(str(LC),symindex)
        symindex+=1
        deteckmn(k)

    symbol()
    littab()



ipf.close()
lit.close()
sym.close()