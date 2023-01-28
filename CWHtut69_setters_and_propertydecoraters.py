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


hindustani_supporter = Employee("Hindustani", "supporter")
nikhil_pandey = Employee("Nikhil", "Pandey")
print(nikhil_pandey.explain())

print(hindustani_supporter.printemail)
hindustani_supporter.fname = "US"
print(hindustani_supporter.printemail)

hindustani_supporter.printemail = "this.that@codewithharry.com"
print(hindustani_supporter.printemail)

del hindustani_supporter.printemail
print(hindustani_supporter.printemail)
hindustani_supporter.printemail = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.printemail)
