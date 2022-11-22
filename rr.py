def waiting_time(at,bt,n):

    rt=[0]*n
    wt=[0]*n
    for i in range(n):
        rt[i]=bt[i]
    q=2
    cur_t=0
    while (1):
        proc_remain=True

        for i in range(n):
            if rt[i]>0:
                proc_remain=False

                if rt[i]>q:
                    cur_t+=q
                    rt[i]-=q

                else:
                    cur_t+=rt[i]
                    rt[i]=0
                    wt[i]=cur_t-bt[i]

        if proc_remain==True:
            break
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

wt=waiting_time(at,bt,n)
tat=tat(wt,n,bt)
print(wt)