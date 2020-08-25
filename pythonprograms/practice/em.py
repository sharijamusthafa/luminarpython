
class employee:
    def __init__(self,eid,ename,esal):
        self.id=eid
        self.name=ename
        self.esal=esal
    def printvalues(self):
        print("name",self.name)
        print("salary",self.esal)
    def __str__(self):
        return self.name


f = open("edetails", "r")
for emp in f:
    #print(employee)
    data=emp.rstrip("\n").split(",")
    eid=data[0]
    ename=data[1]
    esal=data[2]
    obj=employee(eid,ename,esal)
    obj.printvalues()