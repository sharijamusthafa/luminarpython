list=[1,2,3,6,7,4,33]
n=int(input("enter the number to search"))
flag=1
for i in list:
    if(i==n):
        flag=0
        break
    else:
        flag=1
if(flag>0):
    print("element not found=",n)
else:
    print("element  found",n)