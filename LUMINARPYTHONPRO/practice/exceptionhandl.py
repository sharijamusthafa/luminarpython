num1=int(input("enter a number"))
num2=int(input("enter a number"))
list=[1,2,3,4,5]
try:
    res=num1/num2
    print("result",res)
    pos=int(input("enter index position"))
    print(list[pos])
    print("we have database transaction")
except Exception as e:
    print(e.args)
