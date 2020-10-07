num1=int(input("enter num"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if((num1>num2)&(num1>num3)):
    if((num2>num3)):
        print("num2g")
    else:
        print("num3g")
elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print("num1g")
    else:
        print("num3g")
elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print("num1g")
    else:
        print("num2g")