from re import *
rule='[Kk][Ll][0-9]{2}[a-z]{2}\d{4}'
varname=input("enter variable name")
mat=fullmatch(rule,varname)
if(mat !=None):
    print("valid")
else:
    print("invalid")