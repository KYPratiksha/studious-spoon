#
# l = 10
#
#
# def function(n):
#     # l = 5
#     print(n,"this is me")
#     global l      # global keyword gives its access to functon
#     l = l + 34    # local variable cant read global variable
#                   # local variable is used in read only
#     print(l)
#
#
#
# function("I have printed")
# print(l)







def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan",x)
    rohan()
    print("after calling rohan", x)
harry()
print(x)
