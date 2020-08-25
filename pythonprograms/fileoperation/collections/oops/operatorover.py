class Book:
    def __init__(self,page):
        self.page=page
    def __add__(self,other):
        return Book(self.page+other.page)
    def __str__(self):
        return str(self.page)
oj=Book(100)
obj=Book(200)
#print(oj+obj)
obb=Book(300)
print(oj+obj+obb)