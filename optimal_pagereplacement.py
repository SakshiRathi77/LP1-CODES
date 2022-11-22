print("This is page replacement by optimal")

pages=int(input("enter total no. of pages required :"))
frame=int(input("enter the size of frame in RAM :"))

top=0
page_bucket=[]
page_fault=0
hnm="hit"


s=list(map(int,input().split()))
for i in range(len(s)):
    future_app=[None for _ in range(frame)]
    if s[i] not in page_bucket:
        if len(page_bucket)<frame:
            page_bucket.append(s[i])
        else:
            flag=0
            for j in page_bucket:
                if j not in s[i+1:]:
                    pos=page_bucket.index(j)
                    page_bucket[pos]=s[i]
                    flag=1
                    break
                else:
                    future_app[page_bucket.index(j)]=s[i+1:].index(j)
            if flag==0:
                far_most=max(future_app)
                ind=future_app.index(far_most)
                page_bucket[ind]=s[i]
        page_fault+=1
        hnm="miss"

    else:
        hnm="hit"
    print("\n|---|")
    for i in range(len(page_bucket)):
        print("|",page_bucket[i],"|")
   
    print("|---|\n")
    print("it is",hnm)


print("total page_fault =",page_bucket)


            
                
