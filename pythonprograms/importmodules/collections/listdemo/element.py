lst=[1,2,3,4,5,6,7,8,9]
ele=int(input("enter element"))#6
flag=0
for i in lst:#1
    if(i==ele):#lst[6]
       flag=1
       break
    else:
        flag=0

if(flag>0):
    print("ele found",ele)
else:
    print("not found")
