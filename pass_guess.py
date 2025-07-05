import random 

easy_word = ["apple", "tiger", "house", "table", "mango", "water"]
medium_word = ["dentist", "balloon", "blanket", "monster", "capture", "science", "laptop", "picture"]
hard_word = ["whispering", "dangerous", "algorithm", "crocodile", "nightmare", "microwave"]

print("Welcome to password guessing game")
print("Choose difficulty level:-  easy, medium, hard")

level = input("Tell your response:- ").lower()
if level == "easy":
    secret = random.choice(easy_word)
elif level == "medium":
    secret = random.choice(medium_word)
elif level == "hard":
    secret = random.choice(hard_word)
else:
    print("Invalid! By default level is 'easy'")
    secret = random.choice(easy_word)


attempt = 0
print("\nGUESS THE WORD")

while True:
    ans = input("Your answer:-")
    attempt += 1

    if ans == secret:
        print(f"\nCongratualtion! You guess the answer in {attempt} attempt")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(ans) and ans[i] == secret[i]:
            hint += ans[i]
        else:
            hint +='_'
    print(f'Hint:- {hint}')
print("Game over")
