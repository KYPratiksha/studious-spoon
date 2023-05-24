# SNAKE-WATER-GUN
# IT'S A GAME BETWEEN COMPUTER AND USER TOTAL 10 CHANCES ARE GIVEN
import random

print("SNAKE-WATER-GUN GAME!!")
print("s.snake\nw.water\ng.gun")
list = ["snake", "water", "gun"]
# TOTAL CHANCES
c = 10
# INITITAL USER POINTS = 0
u = 0
# INITITAL COMPUTER POINTS = 0
co = 0
while (c >= 1):
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
