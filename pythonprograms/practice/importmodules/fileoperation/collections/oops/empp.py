import functools
class Employee:
    def __init__(self,id,name,des,sal):
        self.id=id
        self.name=name
        self.des=des
        self.sal=sal
    def printemp(self):
        print("name=",self.name)
        print("designation=",self.des)
        print("sal",self.sal)

    def __str__(self):
        #return self.name+self.id+self.sal+self.des
        return self.name+self.sal
f=open("edetails","r")
lst=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    des=data[2]
    sal=data[3]
    obj=Employee(id,name,des,sal)
    #obj.printemp()
    lst.append(obj)
#for emp in lst:
    #print(emp)
    #print(emp.name.upper())


s2= list(map(lambda emp: emp.name.upper(),lst))
print(s2)
   # if(int(emp.sal)>25000):
     #   print(emp)
    #ss= filter(lambda emp: (int(emp.sal)>20000), lst)
#print(ss)
mm = list(filter(lambda empp: int(empp.sal) > 20000, lst))
#print(mm)
for lss in mm:
    print(lss)
sss= list(map(lambda d: int(d.sal)+5000,lst))
print(sss)

highestsal=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,list(map(lambda empp:empp.sal,lst)))
print(highestsal)
maxsalem=list(filter(lambda em:em.sal==highestsal,lst))
for emm in maxsalem:
    print(emm)

