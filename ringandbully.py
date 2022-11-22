def ring():
    global process
    global p_status
    global cordinator
    while (True):
        print("enter any of the following>>>>>>>>>>:")
        print("1. CRASH ")
        print("2. ACTIVATE ")
        print("3. DISPLAY")
        print("4. EXIT")
        ch1=int(input("enter your choice :"))
        if ch1==1:
            ch=int(input("enter the process you want to crash :"))
            if (p_status[ch-1]):
                p_status[ch-1]=0
                print("crashed successfully!!")
            else:
                print("print process is dead already !!")
            
            if cordinator==ch:
                print("cordinator is crashed !!")

                inititor=int(input("enter the process whch detect the crash:"))
                subcordinator=[inititor]

                i=1
                while(i<len(process)):
                    gid=(inititor+i)%(len(process)+1)
                    if (p_status[gid-1]):
                        subcordinator.append(gid)
                        print("active_list send to ",gid)
                    i+=1
                
                cordinator=max(subcordinator)
                print(cordinator,"is declared as winner of election") 
                # yeeeppppyyyy....jhumo re nacho re


        elif ch1==2:
            ch=int(input("enter the process you want to ACTIVATE :"))
            if( p_status[ch-1]):
                print("process is already alive")
            else:
                p_status[ch-1]=1
                print("process is activate!")
            if (ch==len(process) or cordinator<ch):
                cordinator=ch
                print(cordinator,"is declared as winner of election")

        elif ch1==3:
            display(process,p_status)
        elif ch1==4:
            break
        
        else:
            print("enter the valid choice !!!")



def bully():
    global process
    global p_status
    global cordinator
    while (True):
        print("enter any of the following>>>>>>>>>>:")
        print("1. CRASH ")
        print("2. ACTIVATE ")
        print("3. DISPLAY")
        print("4. EXIT")
        ch=int(input("enter your choice :"))
        if ch==1:
            display(process,p_status)
            crash_p=int(input("enter the process you want to crash :"))
            if (p_status[crash_p-1]==0):
                print("process is already dead !!")
            else:
                p_status[crash_p-1]=0
                print("process crashed successfully!!")

            if cordinator==crash_p:
                print("cordinator is crashed!")
                ch=int(input("enter the process_id which detect the crash :"))
                i=ch+1
                subcordinator=ch
                flag=0
                while(i<len(process)):
                    print("message send from ",ch,"to process",i)
                    if p_status[i-1]:
                        subcordinator=i
                        print("response send to ",ch+1)
                        flag=1
                    print()
                    i+=1
                if flag==1:
                    print("2 nd response send to",ch,",",subcordinator,"is elected")
                
                cordinator=subcordinator
            
        elif ch==2:
            ch=int(input("enter rhre process you want to activate :"))
            if p_status[ch-1]==0:
                p_status[ch-1]=1
                print("activated succesfully")
            else:
                print("process already alive")
            
            if ch==len(process):
                cordinator=ch
            else:
                if cordinator>ch:
                    print("cordinator remains unchanged")
                    print("send msg to all process")
                    print("cordinator is",cordinator)

                else:
                    i=ch+1
                    subcordinator=ch
                    while(i<len(process)):
                        print("message send from ",ch,"to process",i)
                        if p_status[i-1]:
                            subcordinator=i
                            print("response send to ",ch+1)
                        i+=1
                    print()
            
                    cordinator=subcordinator
                    


        elif ch==3:

            display(process,p_status)
        elif ch==4:
            break
        
        else:
            print("enter the valid choice !!!")


    

def display(process,p_status):
    global cordinator
    print("--------------------------------------------------------\n")
    print("****************process dashborad**********************\n")
    print("PROCESS NO.\t ",end=' ')
    for i in process:
        print(i, end="\t")
    print()
    print("PROCESS sta\t",end=' ')
    for i in p_status:
        print(i, end=" \t")
    
    print("\n--------------------------------------------------------\n")
    print("cordinator is ",cordinator)

def choice():
    while (True):
        print("enter any of the following>>>>>>>>>>:")
        print("1. RING ALGORITHM ")
        print("2. BULLY ALGORITHM ")
        print("3. QUIT")
        ch=int(input("enter your choice :"))
        if ch==1:
            ring()
            
        elif ch==2:
            bully()
        
        elif ch==3:
            exit()
        
        else:
            print("enter the valid choice !!!")


process=[]
n=int(input("enter total no. of prrocesses :"))
p_status=[0]*n
cordinator=0
for i in range(n):
    process.append(i+1)
    status=int(input("enter the status of process (0 for dead/1 for alive) :"))
    p_status[i]=status
    if p_status[i]:
        cordinator=i+1


display(process,p_status)
choice()