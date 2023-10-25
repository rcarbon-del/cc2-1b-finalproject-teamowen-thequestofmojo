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
user = input('"Young one, what is your name?" ')
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

print("You look around the room and see a book.")
time.sleep(2)
print()
print("The book says,")
time.sleep(1.5)
print()
print(""""Nexus: The World of Peace"
    The blessed world brought by the gods. Ever since the start 
of time, the world was at peace. The gods have given the people 
of Nexus the power of magic. The people of Nexus used magic to 
help the world. The world was at peace for a thousand years. But, 
the gods have left the world of Nexus. However, the gods left a 
gift for the people of Nexus. The gift was the magical stone, 
Citrine. Citrine is the most powerful and dangerous 
object in the world. It gave the people the ability to use 
magic without the help of gods.""")
time.sleep(1)
print()
end = input("Press enter to flip to the next page...")
clearOutput(16)

print("You flip the page, it says,")
time.sleep(1.5)
print()
print(""""The Fall of Nexus"
The world of Nexus was at peace for a thousand years. Until""")