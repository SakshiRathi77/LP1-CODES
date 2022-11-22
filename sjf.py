def waitingtime(at,bt,n):
    rt=[0]*n
    wt=[0]*n
    for i in range(n):
        rt[i]=bt[i]


    pro_complete=0
    minm=999999
    p_id=0
    cpu_stat=False
    current_time=0


    while(pro_complete!=n):

        for i in range(n):
            if (rt[i]<minm and rt[i]>0 and at[i]<=current_time ):
                minm=rt[i]
                p_id=i
                cpu_stat=True

        if (cpu_stat==False):
            current_time+=1
            continue

        rt[p_id]-=1
        minm=rt[p_id]
        if(minm==0):
            minm=99999


        if(rt[p_id]==0):
            pro_complete+=1
            cpu_stat=False

            fint=current_time+1
            wt[p_id]=fint-at[p_id]-bt[p_id]

            if (wt[p_id]<0):
                wt[p_id]=0
        current_time+=1

    return wt

                


def tat(wt,n,bt):
    tat=[0]*n
    for  i in range(n):
        tat[i]=wt[i]+bt[i]
    
    return tat


def input1():
    at=[]
    pn=[]
    bt=[]
    n=int(input("enter total no. of process :"))
    for i in range(n):
        p1=int(input("Enter the process no. :"))
        a1=int(input("Enter the arrival time :" ))
        b1=int(input("enter the burst time of process:"))

        pn.append(p1)
        at.append(a1)
        bt.append(b1)

    return n,pn,at,bt


n,pn,at,bt=input1()
a=list(zip(pn,at,bt))
a.sort(key=lambda x:x[1])
print(a)

for i in range(len(a)):
    pn[i]=a[i][0]
    at[i]=a[i][1]
    bt[i]=a[i][2]

print("pn no",pn)
print("at is",at)
print("bt is ",bt)
wt=waitingtime(at,bt,n)
tat=tat(wt,n,bt)

print("waiting time :",wt)
print("tat is ",tat)