list=[]
list1=[]
n=int(input("enterthe limit:"))
print("enter the no.:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
for i in range(0,n-1):
    list1.append(list[i]+list[i+1])
list1.append(list[-1]+list[0])
list1.sort(reverse=True)
print(list1)