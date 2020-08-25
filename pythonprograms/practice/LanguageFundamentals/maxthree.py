num1=int(input("enter num"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if((num1>num2)&(num1>num3)):
    print("num1")
elif((num2>num1)&(num2>num3)):
    print("num2g")
elif((num1==num2)&(num2==num3)&(num1==num3)):
    print("equal")
else:
    print("num3g")