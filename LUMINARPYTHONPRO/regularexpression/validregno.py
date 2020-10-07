from re import *
list=[]
rule='[Kk][Ll][0-9]{2}[a-z]{2}\d{4}'
f=open("regno","r")
#mat=finditer(rule,"f")
for line in f:
    data=line.rstrip("\n")
    mat=fullmatch(rule,data)
    if(mat !=None):
        list.append(data)
    else:
        pass
#print("validregno",list)
f1=open("regnoo","w")
for item in list:
    f1.write("%s\n"% item)
f1=open("regnoo","r")

for d in f1:
    print(d)




