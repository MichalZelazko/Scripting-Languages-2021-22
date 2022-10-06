import random

goal = random.randint(1, 20)
while True:
    guess = input("Guess a number: ")
    if not guess.isdigit():
        print("Entered number has to be an integer")
        continue
    else:
        guess = int(guess)
    if guess > goal:
        print("Your number is too big")
    elif guess < goal:
        print("Your number is too small")
    else:
        print("Congratulations! Your guess was correct")
        break
