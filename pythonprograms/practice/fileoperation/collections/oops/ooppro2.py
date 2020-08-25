class Employee:
    def __init__(self, id, name, desig, salary):
        self.id = id
        self.name = name
        self.designation = desig
        self.salary = salary

    def printValues(self):
        print(self.id)
        print(self.name)
        print(self.designation)
        print(self.salary)
    def __str__(self):
        return self.name

obj1 = Employee(1001,"rahul","tester",10000)
obj2= Employee(1001,"aju","tester",20000)
obj3 = Employee(1001,"manu","tester",30000)
#obj.printValues()
#print(obj.name)
#ls=[]
3ls.append(obj1)
#ls.append(obj2)
#ls.append(obj3)
#for emp in ls:
    #if(emp.salary>22000):
      #  print(emp)

