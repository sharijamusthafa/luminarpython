low=int(input("enter low limit"))
upper=int(input("enter upper limit"))
sumeven=0
sumodd=0
for i in range(low,(upper+1)):
    if(i%2==0):
        sumeven+=i

    else:
        sumodd+=i
print("sumeven",sumeven)
print("sumodd",sumodd)

