f=open("num","r")
list=[]

for num in f:
    #list.append(int(num))
     list.append(int(num.rstrip("\n")))
#res=sum(list)
#print(res)
even=[]
odd=[]
for i in list:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(" ")
print(odd)