num1=int(input("enter a number"))
num2=int(input("enter a number"))
try:
    res=num1/num2
    print("result",res)

    print("we have database transaction")
except Exception as e:
    num1=int(input("enter a no"))
    num2=int(input("enter a no"))
    try:
        res=num1/num2
        print(res)
    except Exception as e:
        print(e.args)
finally:
    print("success")