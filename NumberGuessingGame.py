import random
win_num = random.randint(1,101)
while True:
    guess = int(input("Guess a number from 1-100: "))
    if guess == win_num:
        print("YOU WON!!!!!!!!")
        break
    elif guess > win_num:
        print("Lower")
    elif guess < win_num:
        print("Higher")