employees=[[1001,"arjun",10000],[1002,"kiran",20000],[1003,"jon",20000],[1004,"kishan",30000]]
sum=0
for emp in employees:
    if(emp[2]>15000):
       # print(emp[1])
       sum=sum+emp[2]
print(sum)