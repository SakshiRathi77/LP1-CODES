print("This is page replacement by LRU")

pages=int(input("enter total no. of pages required :"))
frame=int(input("enter the size of frame in RAM :"))

top=0
page_bucket=[]
stack_ru=[]
page_fault=0
hnm="hit"

s=list(map(int,input().split()))
for i in range(len(s)):
    if s[i] not in page_bucket:
        if len(page_bucket)<frame:
            page_bucket.append(s[i])
            stack_ru.append(page_bucket.index(s[i]))
        else:
            a=stack_ru.pop(0)
            page_bucket[a]=s[i]
            stack_ru.append(a)
        page_fault+=1
        hnm="miss"
    
    else:
        pos=page_bucket.index(s[i])
        stack_pos=stack_ru.index(pos)

        stack_ru.pop(stack_pos)
        stack_ru.append(pos)
        hnm="hit"


    print("\n|---|")
    for i in range(len(page_bucket)):
        print("|",page_bucket[i],"|")
   
    print("|---|\n")
    print("it is",hnm)


    
