def calcu(**args):
    #print(args)
    sum=0
    mul=1
    print("1.addition\n2.multiplication")

    n=int(input("enter ypur choice"))
    if(n==1):
        for k, v in args.items():
            sum+=v
        print("result=", sum)
    if(n==2):
            for k, v in args.items():
                mul*=v

            print("multiplication=",mul)
calcu(num1=12,num2=22,num3=15)