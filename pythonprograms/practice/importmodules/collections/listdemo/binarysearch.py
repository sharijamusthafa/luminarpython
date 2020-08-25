list=[10,11,12,13,14,15,2,3,4]
list.sort()
print(list)

low=0
upp=len(list)-1
ele=int(input("enter ele"))
flag=0
while(low<=upp):
        mid=(low+upp)//2
        if(ele>list[mid]):
            low=mid+1
        elif(ele<list[mid]):
             upp=mid-1
        elif(ele==list[mid]):
            flag=1
            break
if(flag>0):
    print("ele found")
else:
    print("not found")
