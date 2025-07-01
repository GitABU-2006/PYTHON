# RANDOM NUMBER GUESING GAME
import random
num = random.randint(1,10)
tries=0
print("IT'S A SIMPLE GUESSING GAME")
while True:
    guess = int(input("guess a number between 1 to 10:-"))
    if num == guess :
        tries+=1
        print(f"you are right it's  {num}")
        break
    elif num<guess:
        print("go a little lower")
        tries+=1
    elif num>guess:
        print("go a little higher")
        tries+=1
    else:
        tries+=1
        print("you are wrong")
if tries ==1:
    print("impressive you guessed it right in one go")
print(f"attempt {tries} ")
