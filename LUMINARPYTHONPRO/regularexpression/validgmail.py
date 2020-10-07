from re import *
list=[]
rule='\w*\w@gmail.com'
f=open("mailid","r")
#mat=finditer(rule,"f")
for line in f:
    data=line.rstrip("\n")
    mat=fullmatch(rule,data)
    if(mat !=None):
        list.append(data)
    else:
        pass

f1=open("mailidd","w")
for item in list:
    f1.write("%s\n"% item)
f1=open("mailidd","r")

for d in f1:
    print(d)

