class Dad:
    basketball = 1

class Son(Dad):
    basketball = 2
    dance = 9
    def isdance(self):
        return f"I can dance {self.dance} times"

class Grandson(Son):
    dance = 6
    guitar=2
    def isdance(self):
        return f"I can dance {self.dance} no of times"

larry = Dad()
harry = Son()
carry = Grandson()

print(harry.basketball)

