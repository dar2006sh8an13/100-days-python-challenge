#Number Guessing game 
import random

num = random.randint(1,50)
while True:
    guess = int(input("guess the number (1-50):"))
    if guess == num:
        print("correct!")
    elif guess <num:
        print ("too low!")
    else:
        print("too high!")