# THIS PROGRAM IS USED TO CREATE  HEALTH MANAGMEENT SYSTEM FOR PROGRAMMERS
#THREE TYPES OF INPUT CAN BE GIVEN:
# first input = retrieve or log
# second input = client name
# third input= diet or excersise
# HERE YOU WILL NEED SIX TEXT FILES:
# 1)HARRY EXCERCISE AND DIET FILE
# 2)HAMMAD EXCECISE AND DIET FILE
# 3)ROHAN EXCERCISE AND DIET FILE



print("HEALTH MANAGEMENT SYSTEM")
print("1.Harry\n2.Hammad\n3.Rohan")
client_name = input("enter client number 1/2/3: ")
print("1.Retrieve\n2.Log")
retrieve_log = input("you want to retrieve or log: ")
print("1.Exercise\n2.Diet")
diet_excersise = input("enter diet or exercise : ")


def getdate():
    import datetime
    return datetime.datetime.now()


if client_name == '1':
    if retrieve_log == '1':
        if diet_excersise == '1':
            f = open("harry_exercise.txt")
            read = f.read()
            print(str(getdate()) + read)
        elif diet_excersise == '2':
            f = open("harry_diet.txt")
            read = f.read()
            print(str(getdate()) + read)

    elif retrieve_log == '2':
        if diet_excersise == '1':
            f = open("harry_exercise.txt", 'a')
            statement = input("enter what you want to log: ")
            print(str(getdate()))
            w = f.write(statement)
        elif diet_excersise == '2':
            f = open("harry_diet.txt", 'a')
            statement = input("enter what you want to log: ")
            print(getdate())
            w = f.write(statement)

if client_name == '2':
    if retrieve_log == '1':
        if diet_excersise == '1':
            f = open("hammad_exercise.txt.txt")
            read = f.read()
            print(str(getdate()) +read)
        elif diet_excersise == '2':
            f = open("hammad_diet.txt")
            read = f.read()
            print(str(getdate()) +read)

    elif retrieve_log == '2':
        if diet_excersise == '1':
            f = open("hamaad_exercise.txt", 'a')
            statement = input("enter what you want to log: ")
            print(str(getdate()))
            w = f.write(statement)
        elif diet_excersise == '2':
            f = open("hammad_diet.txt", 'a')
            statement = input("enter what you want to log: ")
            print(str(getdate()))
            w = f.write(statement)

if client_name == '3':
    if retrieve_log == '1':
        if diet_excersise == '1':
            f = open("rohan_exercise.txt")
            read = f.read()
            print(str(getdate()) + read)
        elif diet_excersise == '2':
            f = open("rohan_diet.txt")
            read = f.read()
            print(str(getdate()) + read)

    elif retrieve_log == '2':
        if diet_excersise == '1':
            f = open("rohan_exercise.txt", 'a')
            statement = input("enter what you want to log: ")
            print(str(getdate()))
            w = f.writelines(statement)
        elif diet_excersise == '2':
            f = open("rohan_diet.txt", 'a')
            statement = input("enter what you want to log: ")
            print(str(getdate()))
            w = f.writelines(statement)
