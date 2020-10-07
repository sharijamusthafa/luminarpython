class person:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def printValue(self):
        print(self.id)
        print(self.name)
    def __str__(self):
        return self.name
obj=person(1100,"ajay",1000)
print(obj)