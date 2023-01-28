class Employee:          #class
    no_of_leaves = 8      #class variable
    pass

harry = Employee()         #instance
rohan = Employee()          #instance

harry.name = "Harry"        #instance attributes
harry.age = 12

rohan.name = "Rohan"       #instance attribute
rohan.age = 45

print(harry.no_of_leaves)         #both harry and rohan sharing class variable
print(rohan.no_of_leaves)

harry.no_of_leaves = 7           #created a new instance in harry object
print(harry.no_of_leaves)

print(Employee.no_of_leaves)       #value of instance remains same in class

Employee.no_of_leaves = 9      #value of instance variable can be changed only by class
print(Employee.no_of_leaves)

print(harry.no_of_leaves)     #value remains same in object instance