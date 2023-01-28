class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    def explain(self):
        return f"This emplyoee is {self.fname} {self.lname}."

    @property
    def printemail(self):
        if self.fname == None or self.lname == None:
            print("Email is not set")
        return f"Email is {self.fname}.{self.lname}@codewithharry.com."

    @printemail.setter
    def printemail(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @printemail.deleter
    def printemail(self):
        self.fname = None
        self.lname = None

skillf = Employee("Skill", "F")
print(skillf.printemail)

print(type(skillf))
o = "this is a string"
print(type(o))
print(dir(skillf))
print(id("this that"))

import inspect
print(inspect.getmembers(skillf))