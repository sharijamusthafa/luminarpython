def add(**args):
    print(args)
args={"num1":10,"num2":20,"num3":30}
sum=0
for k,v in args.items():
    sum+=v
    print("sum",sum)

