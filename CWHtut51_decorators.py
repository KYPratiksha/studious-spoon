# def function1():
#     print("subscribe now")
# func2 = function1
# del function1
# func2()


# def funcret(num):
#     if num == 0:
#         return print
#     if num== 1:
#         return int
#
# a = funcret(0)
# print(a)


# def executer(func):
#     func("hi")
# executer(print)



def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec

@dec1                   #works same as who_is_harry = dec1(who_is_harry)
def who_is_harry():
    print("HArry")
# who_is_harry = dec1(who_is_harry)
who_is_harry()
