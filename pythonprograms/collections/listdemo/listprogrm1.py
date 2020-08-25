even=[]
odd=[]
ls=[]
for i in range(50,70):
    ls.append(i)
print(ls)
for i in ls:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("odd",odd)
print("even",even)

