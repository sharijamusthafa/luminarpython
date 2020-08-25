mylist=[1,2,1,3,6,4,3]
newlist=[]
for i in mylist:
    if i not in newlist:
        newlist.append(i)
print(newlist)