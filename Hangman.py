import time
from time import sleep

name=input("What is your name?: ")
print("Hello, " + name + "!")
print("Get Ready!")

time.sleep(2)

print("Are you ready to play hangman?")
time.sleep(2)

print("Let's go!")
time.sleep(2)

word = "Flower"
wrd=''
chance = 10

while chance > 0:
    failed = 0
    for char in word:
        if char in wrd:
            print(char)
        else:
            print("_")
            failed += 1
    
    if failed == 0:
        print("You won!")
        print("Congratulations")
        break
    
    guess = input("Guess a letter: ")
    
    wrd=wrd+guess
    
    if guess not in word:
        chance -= 1
        print("Wrong guess...Try again")
        print("You have",chance,"more turns")
        
        if chance == 0:
            print("You lose! Try next time")