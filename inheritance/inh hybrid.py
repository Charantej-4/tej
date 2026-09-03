class A():
    def method(self):
        print("A method")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
d=D()
d.method()