from re import *
rule='\w*[@]\w{5}[.]\w{3}'
varname=input("enter variable name")
mat=fullmatch(rule,varname)
if(mat !=None):
    print("valid")
else:
    print("invalid")