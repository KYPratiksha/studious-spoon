class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am a instance variable in class A"
        self.classvar1 = "Instance variable of Class A"
        self.special = "I am special"

class B(A):
    classvariable2 = "I am class variable in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am a instance variable in class B"
        self.classvar1 = "Instance variable of Class B"
        # super().__init__()

a = A()
b = B()
print(b.var1)
print(b.classvar1)
print(b.special)