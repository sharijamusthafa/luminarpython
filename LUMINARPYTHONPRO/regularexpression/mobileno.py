from re import *
rule='\d{10}'
mobno=input("enter no.")
mat=fullmatch(rule,mobno)
if(mat !=None):
    print("valid")
else:
    print("invalid")