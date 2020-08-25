lst=[10,10,40,20,10,30,15]
list=[]
lst.sort()
last=len(lst)
print(lst)

for i in range(0,last-1):
    tem=lst[i]
    if(tem!=lst[i+1]):
        list.append(tem)


if(lst[last-2]==lst[last-1]):
    list.append(lst[last-1])
else:
    list.append(lst[last-1])
print(list)
