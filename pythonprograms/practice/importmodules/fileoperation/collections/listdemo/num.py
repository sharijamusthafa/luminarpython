list=[]
print("Enter three number:")
n=3
for j in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
list1=[]
f=0
for i in list:
    index=list.index(i)
    if(index==0):
        f=list[1]+list[2]
        list1.append(f)
    elif(index==1):
        f = list[0]+list[2]
        list1.append(f)
    elif (index==2):
        f = list[0]+list[1]
        list1.append(f)
    else:
        break
print(list1)