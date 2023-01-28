class A:
    def met(self):
        print("I am from class A")


class B(A):
    # def met(self):
    #     print("I am from class B")
    pass


class C(A):
    # def met(self):
    #     print("I am from class C")
    pass

class D(B, C):
    # def met(self):
    #     print("I am from class D")
    pass

a = A()
b= B()
c = C()
d = D()
print(d.met())