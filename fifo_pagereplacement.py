print("This is page replacement by FIFO")

pages=int(input("enter total no. of pages required :"))
frame=int(input("enter the size of frame in RAM :"))

top=0
page_bucket=[]

page_fault=0
hnm="hit"

s=list(map(int,input().split()))
for i in range(len(s)):
    if s[i] not in page_bucket:
        if len(page_bucket)<frame:
            page_bucket.append(s[i])
        else:
            page_bucket[top]=s[i]
            top=(top+1)%frame
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

        


