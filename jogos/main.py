import random

print("**********************************")
print("Welcome to the game Guessing!")
print("**********************************")

secret_number = random.randrange(1, 101)
total_chances = 0
score = 100

print("Chose a level:")
print("(1) Easy, (2) Medium, (3) Hard.")

level = int(input("level: "))

if level == 1:
    total_chances = 20
elif level == 2:
    total_chances = 10
elif level == 3:
    total_chances = 5
else:
    print("level not available")

for chance in range(1, total_chances + 1):
    print("Chance number {} de {}".format(chance, total_chances), end="\n")
    guess = input("Type your number between 1 and 100: ")
    number = int(guess)
    print("You type ", guess)

    if number < 1 or number > 100:
        print("Try a number between 1 and 100")
        continue

    right = secret_number == number
    higher = secret_number > number
    lower = secret_number < number
    diference = abs(secret_number - number)
    finalscore = score - diference

    if right:
        print("You Right! Your Score is {}".format(finalscore))
        break
    else:
        if higher:
            print("You Failed!, number is higher!")
        elif lower:
            print("You Failed, number is lower!")

print("End Game!")
