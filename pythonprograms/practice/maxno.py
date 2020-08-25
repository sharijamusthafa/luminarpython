num1=int(input("enter no"))
num2=int(input("enter no"))
num3=int(input("enter no"))
if((num1>num2)&(num1>num3)):
    t=num1
    if(num2>num3):
        tt=num2
        ttt=num3
        print(ttt,tt,t)
    else:
        f=num3
        ff=num2
        print(ff,f,t)
elif((num2>num1)&(num2>num3)):
    s=num2
    if(num1>num3):
        ss=num1
        sss=num3
        print(sss,ss,s)
    else:
        g=num3
        gg=num1
        print(gg,g,s)
elif((num3>num1)&(num3>num2)):
    k=num3
    if(num1>num2):
        kk=num1
        kkk=num2
        print(kkk,kk,k)
    else:
        l=num2
        ll=num1
        print(ll,l,k)
else:
    pass