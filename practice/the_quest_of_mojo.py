import random
import time

# Clear output
def clearOutput(numberOfLines: int):
    cursorUpOne = '\x1b[1A'
    erase = '\x1b[2K'
    for _ in range(numberOfLines):
        print(cursorUpOne + erase, end='')

#Welcome screen
def welcomeScreen():
    print()
    print("Welcome to the Quest of Mojo!")
    time.sleep(2)
    print()
    print("""The Quest of Mojo is a role-playing game (RPG) that takes place 
in a post-apocalyptic Nexus, beginning in the year 1751.""")
    time.sleep(2)
    print()
    print("1. Start")
    print("2. Credits")
    print("3. Quit")
    print()
    titleChoice = input("> ")
    if titleChoice == "1":
        clearOutput(11)
    elif titleChoice == "2":
        clearOutput(11)
        print("""The Quest of Mojo was created by:
        
    Bulatao, Chris Owyn
    Carbonel, Radge Daryll
    Carbonell, Jennylyn
    Cero, Wyatt
              
For completion of the requirements for the course,
Introduction to Computer Programming | CITCS 1B,
taught by Sir Jerry Junior Pacalso.""")
        print()
        end = input("Press enter to return...")
        clearOutput(12)
        welcomeScreen()

    elif titleChoice == "3":
        quit()
    else:
        print("Invalid choice.")
        time.sleep(1)
        clearOutput(11)
        welcomeScreen()

welcomeScreen()
print("The Quest of Mojo")
print()
time.sleep(1)

#Character creation
print("As you open your eyes, the light of day shines through your window.")
time.sleep(5)
clearOutput(1)
time.sleep(3)

print("You wake up in a small room.")
time.sleep(5)
clearOutput(1)

print("Suddenly, You hear someone speaking to you.")
time.sleep(1.5)
print()
user = input('"Master, what is your name?" ')
clearOutput(3)

print("You reply, " + user + ".")
time.sleep(5)
clearOutput(1)

print("The voice replies,")
time.sleep(1.5)
print()
print('"Ah, ' + user + ' , I see you that are awake."')
time.sleep(5)
clearOutput(3)

print("You look around the room and see a tablet.")
time.sleep(2)
print()
print("The tablet says,")
time.sleep(1.5)
print()
print('"You are in the year 1751, in the post-apocalyptic Nexus."')