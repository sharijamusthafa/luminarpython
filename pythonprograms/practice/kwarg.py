def add(**args):
    print(args)
res=0
args={"num1":10,"num2":20,"num3":30}
for k,v in args.items():
    res+=v
print("res",res)
