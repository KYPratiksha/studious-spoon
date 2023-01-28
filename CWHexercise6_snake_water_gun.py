# s - snake
# w = water
# g = gun
# snake + water = snake
# water + gun = water
# snake + gun = gun
#  10 choice
#  while loop


import random

print("SNAKE-WATER-GUN GAME!!")
print("s.snake\nw.water\ng.gun")
list = ["snake", "water", "gun"]
c = 10
u = 0
co = 0
while (c >= 1):
    # c = 0
    user_inp = input("enter your choice: ")
    computer_input = random.choice(list)
    if user_inp == 's' and computer_input == 'water':
        print("computer choice: ", computer_input)
        print("user wins!")
        u += 1
        c -= 1
        print("chances left = ", c)
    elif user_inp == 's' and computer_input == 'gun':
        print("computer choice: ", computer_input)
        print("computer wins !")
        co += 1
        c -= 1
        print("chances left : ", c)
    elif user_inp == 's' and computer_input == 'snake':
        print("computer choice: ", computer_input)
        print("same choice made!")
        c -= 1
        print("chances left = ", c)
    elif user_inp == 'w' and computer_input == 'snake':
        print("computer choice: ", computer_input)
        print("computer wins !")
        co += 1
        c -= 1
        print("chances left : ", c)
    elif user_inp == 'w' and computer_input == 'water':
        print("computer choice: ", computer_input)
        print("same choices made!")
        c -= 1
        print("chances left: ", c)
    elif user_inp == 'w' and computer_input == 'gun':
        print("computer choice: ", computer_input)
        print("user wins !")
        u += 1
        c -= 1
        print("chances left : ", c)
    elif user_inp == 'g' and computer_input == 'snake':
        print("computer choice: ", computer_input)
        print("user wins!")
        u += 1
        c -= 1
        print("chances left :", c)
    elif user_inp == 'g' and computer_input == 'water':
        print("computer choice: ", computer_input)
        print("computer wins!")
        co += 1
        c -= 1
        print("chances left : ", c)
    elif user_inp == 'g' and computer_input == 'gun':
        print("computer choice: ", computer_input)
        print("same choices made")
        c -= 1
        print("choices left = ", c)


    else:
        print("invalid input made")
print("user wins: ", u)
print("computer wins : ", co)
