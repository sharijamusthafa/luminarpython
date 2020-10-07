num1=int(input("enter num"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if((num1>=num2)&(num1>=num3)):
    t=num1
    if((num2>=num3)):
        tt=num2
        ttt=num3
        print(ttt,tt,t)
    else:
        f=num3
        ff=num2
        print(ff,f,t)
elif((num2>=num1)&(num2>=num3)):
    s=num2
    if(num1>=num3):
        ss=num1
        sss=num3
        print(sss,ss,s)
    else:
        k=num3
        kk=num1
        print(kk,k,s)
elif((num3>=num1)&(num3>=num2)):
    j=num3
    if(num1>=num2):
        jj=num1
        jjj=num2
        print(jjj,jj,j)
    else:
        ll=num2
        l=num1
        print(l,ll,j)
#else:
  #  print("equal no")
