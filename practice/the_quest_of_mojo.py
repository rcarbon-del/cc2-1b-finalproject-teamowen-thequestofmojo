import random
import time
from turtle import clear

# Clear output
def clearOutput(numberOfLines: int):
    cursorUpOne = '\x1b[1A'
    erase = '\x1b[2K'
    for _ in range(numberOfLines):
        print(cursorUpOne + erase, end='')

#Welcome screen
def welcomeScreen():
    print()
    print()
    print("Welcome to the Quest of Mojo!")
    time.sleep(2)
    print()
    print("""The Quest of Mojo is a role-playing game (RPG) that takes place 
    in a post-apocalyptic Nexus, beginning in the year 1751.""")
    time.sleep(2)
    print()
    print("1. Start")
    print("2. Quit")
    print()
    titleChoice = input("Enter choice: ")
    if titleChoice == "2":
        quit()
    elif titleChoice == "1":
        clearOutput(12)
    else:
        print("Invalid choice.")
        time.sleep(1)
        clearOutput(12)
        welcomeScreen()

welcomeScreen()
print("The Quest of Mojo")
print()
time.sleep(1)
#Character creation
print("You are a young adventurer who lives alone.")
time.sleep(5)
clearOutput(1)


print("As you open your eyes, the light of day shines through your window.")
time.sleep(5)
clearOutput(1)
time.sleep(3)

print("You suddenly hear someone speaking to you.")
time.sleep(1.5)
print()
user = input('"Young one, what is your name?" ')