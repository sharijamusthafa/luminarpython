num1=int(input("enter num"))#10
num2=int(input("enter num2"))#5
num3=int(input("enter num3"))#2


if((num1<num2)&(num1<num3)):#10<5&10<2
    print("min no.=",num1)


elif((num2<num1)&(num2<num3)):
    print("min no",num2)

elif((num3<num1)&(num3<num2)):
    print("min no",num3)

c = num1 + num2 + num3
b = c - min(num1, num2, num3)
d = b - max(num1, num2, num3)
print("middle no", d)

if ((num1 > num2) & (num1 > num3)):
    print("max no.=", num1)


elif ((num2 > num1) & (num2 > num3)):
    print("max no", num2)

elif ((num3 > num1) & (num3 > num2)):
    print("max no", num3)
