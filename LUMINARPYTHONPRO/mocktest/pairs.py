list1=[1,2,3]
list2=[]
k=len(list1)-1
for i in range(0,k):
    f=list1[i],list1[i+1]
    if (f not in list2):
        list2.append(f)
    fff=list1[0],list1[k]
    if(fff not in list2):
        list2.append(fff)
print(list2)