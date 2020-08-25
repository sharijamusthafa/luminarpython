class parent:
    def m1(self):
        print("inside parent")
class child:
    def m2(self):
        print("inside child")
class subchild(child,parent):
    def m3(self):
        print("inside subchild")
obj3=subchild()
obj3.m1()
obj3.m2()
obj3.m3()