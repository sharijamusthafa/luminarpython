class parent:
    def m1(self):
        print("inside parent")
class child(parent):
    def m2(self):
        print("inside child")
class subchild(child):
    def m3(self):
        print("inside subchild")
obj3=subchild()
obj3.m1()
obj3.m2()
obj3.m3()
obj2=child()
obj2.m1()
obj2.m2()
obj1=parent()
obj1.m1()
