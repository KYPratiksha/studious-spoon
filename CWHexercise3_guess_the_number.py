# n=18
# no of guesses = 9
# print no of guesses left
# game over
# print if entered number is less or more than original number
from typing import Union, Any

n = 18
print("Welcome to guess the number game")
print("No. of guesses available: 9")

# c = 1
for c in range(0, 9):
    inp = int(input("enter your number:"))
    c = 9 - c
    print("count left : ", c)
    print("\n")
    if inp == n:
        print("You have guessed it right! You win")
        break
    elif inp < n:
        print("you have entered lesser number")

        # print("count left : ", c)
    elif inp > n:
        print("you have entered larger number")

    # else:
    #     print("invalid input")
        # c = 9-c

print("Game Over!")

    # else:
    #     c = 9 - c
    #     print("count left: " , c)
