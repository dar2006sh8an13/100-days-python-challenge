#Dice roll simulator
import random
while True:
    roll = random.randint(1,6)
    print(f"you rolled:{roll}")
    if input("roll again? (y/n):").lower()!='y':
        break
