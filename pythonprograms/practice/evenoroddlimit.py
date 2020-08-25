n=int(input("enter the limit"))
flag=1
for i in range(2,n+1):
    if(i%2==0):
        flag=0
    else:
        flag=1
if(flag>0):
    print("prime num=",i)
else:
    print("nonprime=",i)
