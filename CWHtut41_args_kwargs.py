# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
# function_name_print("harry", "rohan", "skillf", "hammad")


def funargs(normal, *args, **kw):   # normal argument must be kept before args and then **kwargs
    print(args[1])
    print(type(args))
    for item in args:
        print(item)
    for key, value in kw.items():
        print(f"{key},{value}")


name = ["harry", "rohan", "skillf", "hammad", "pk"]
normal = "I am a programmer"
kw = {"rohan":"moniter", "harry": "programmer" ,"ishan":"coordinator","mihir":"cook"}
funargs(normal, *name, **kw)

