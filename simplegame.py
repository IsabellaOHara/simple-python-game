import random


print("Welcome to Number Guesser! Let's see if you can guess my 3 digit number!")
num = random.randint(100, 999)
listOfNumDigits = [int(i) for i in str(num)]
# print(listOfNumDigits)

print("Code has been generated...")

flag = True
while flag is True:
    guess = int(input("Guess a 3 digit number"))
    listOfGuessDigits = [int(i) for i in str(guess)]
    for i in range(0, 3):
        if guess == num:
            print("yay you got it!")
            flag = False
            break
        elif listOfGuessDigits[i] == listOfNumDigits[i]:
            print("MATCH: You've guess a correct number in the right position")
            i = i + 1
        elif listOfGuessDigits[i] in listOfNumDigits:
            print("CLOSE: You've guessed a correct number but in the wrong position")
            i = i + 1
        elif listOfGuessDigits[i] not in listOfNumDigits:
            print("NOPE: You haven't guessed any of the numbers correctly")
            i = i + 1
        else:
            print("ERROR")
