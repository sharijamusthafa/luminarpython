lo=int(input("enter low limit"))
upper=int(input("enter upper limit"))
sum=0
sum1=0
for i in range(lo,(upper+1)):
    if(i%2==0):
        sum=sum+i

    else:
        sum1=sum1+i
print(sum)
print(sum1)