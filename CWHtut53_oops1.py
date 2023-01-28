# class is made to reduce efforts
# DRY - Do not Repeat Yourself

class Student:      #class
    pass

harry = Student()      #objects
larry = Student()       #objects

harry.name = "Harry"       #attributes
harry.section = 'a'        #attributes
harry.std = 12             #attributes

larry.std = 8
larry.subjects = ["Cs","English"]

print(larry.std)
print(larry.subjects)
print(harry.name)