def calc(*num):
    sum=0
    mult=1
    print("1).ADD\n2)MULTIPLY")
    n=int(input("enter your choice"))
    if(n==1):
        for i in num:
            sum+=i
        print("result=",sum)
    if(n==2):
        for i in num:
            mult*=i
        print("result=",mult)
calc(1,2,3,4,5,6)