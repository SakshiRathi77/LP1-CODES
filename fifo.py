def waiting1(bt,n):
    wt=[0]*n
    wt[0]=0
    
    for i in range(1,n):
        wt[i]=wt[i-1]+bt[i-1]
    return wt


def waiting2(at1,bt1,n1):
    st=[0]*n1
    wt=[0]*n1
    st[0]=0
    for i in range(1,n1):
        st[i]=st[i-1]+bt1[i-1]
    print("service time for",i ,st[i])
    for i in range(n1):
        wt[i]=st[i]-at1[i]
        if wt[i]<0:
            wt[i]=0
    
    return wt

def tatime(bt,wt,n):
    tat=[0]*n
    for i in range(n):
        tat[i]=bt[i]+wt[i]

    return tat
       
def average(wt,tat,n):
    average_wt=sum(wt)/n
    average_tat=sum(tat)/n
    return average_wt,average_tat

def process_input():
    at=[]
    pn=[]
    bt=[]
    process_n=int(input("enter total no. of process :"))
    for i in range(process_n):
        p1=int(input("Enter the process no. :"))
        a1=int(input("Enter the arrival time :" ))
        b1=int(input("enter the burst time of process:"))

        pn.append(p1)
        at.append(a1)
        bt.append(b1)

    return p1,pn,at,bt

def arrival_atzero():
    n,pn,at,bt=process_input()

    wt=waiting1(bt,n)
    tat=tatime(bt,wt,n)
    average_wt,average_tat=average(wt,tat,n)

    print("\tprocess\t wt\t tat \t bt")
    for  i in range (n): 
        print("\t",pn[i],"\t",wt[i],"\t",tat[i],"\t",bt[i])


    print("average waiting time",average_wt)
    print("average tat is ",average_tat)


def arrival_random():
    n1,pn1,at1,bt1=process_input()
    a=list(zip(pn1,at1,bt1))
    a.sort(key=lambda x:x[1])
    print(a)

    for i in range(len(a)):
        pn1[i]=a[i][0]
        at1[i]=a[i][1]
        bt1[i]=a[i][2]

    print("pn no",pn1)
    print("at is",at1)
    print("bt is ",bt1)
    wt1=waiting2(at1,bt1,n1)
    tat1=tatime(bt1,wt1,n1)
    average_wt,average_tat=average(wt1,tat1,n1)

    print("\tprocess\t wt\t tat \t bt")
    for  i in range (n1): 
        print("\t",pn1[i],"\t",wt1[i],"\t",tat1[i],"\t",bt1[i])

    print("average waiting time",average_wt)
    print("average tat is ",average_tat)

arrival_random()
arrival_atzero()

