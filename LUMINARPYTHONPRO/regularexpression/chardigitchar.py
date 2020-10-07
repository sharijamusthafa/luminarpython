from re import *

rule='[a-k][369][a-zA-Z0-9]*'
varname=input("enter variable name")
mat=fullmatch(rule,varname)
if(mat !=None):
    print("valid")
else:
    print("invalid")