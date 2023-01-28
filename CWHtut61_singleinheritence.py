class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
         cls.no_of_leaves = newleaves
    @classmethod
    def from_dash(cls, string):
        # param = string.split("-")
        # print(param)
        # return cls(param[0], param[1], param[2])
        return cls(*string.split("-"))


    @staticmethod
    def printgood(string):
        print("This is good" + string)


class programmer(Employee):
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}. Languages is {self.languages}"



harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan",455,"Student")

shubham = programmer("shubham", 666, "programmer", ["python"])
karan = programmer("karan", 777, "programmer", ["python"])

print(karan.no_of_leaves)
print(shubham.printdetails())
print(karan.printprog())