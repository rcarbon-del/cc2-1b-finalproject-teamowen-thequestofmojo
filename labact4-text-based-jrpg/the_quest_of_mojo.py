from calendar import c
import random
import time

# Variables and functions
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

# Main game
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

print("Suddenly, you hear someone speaking to you.")
time.sleep(1.5)
print()
print('"Young one, what is your name?" ')
print()
user = input("> ")
clearOutput(5)

print("You reply, " + user + ".")
time.sleep(5)
clearOutput(1)

print("The voice replies,")
time.sleep(1.5)
print()
print('"Ah, ' + user + ', I see you that are awake."')
time.sleep(5)
clearOutput(3)

print("You look around the room and see a book.")
time.sleep(2)
print()
print("The book was written in Japanese. However, you are able to read it.")
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
time.sleep(10)
print()
end = input("Press enter to flip to the next page...")
clearOutput(18)

print("You flip the page, it says,")
time.sleep(1.5)
print()
print(""""The Fall of Nexus"
The world of Nexus was at peace for a thousand years. Until
the day came when the gods left the world of Nexus. The people
of Nexus were sad and angry. They wanted the gods to come back.
The people of Nexus started to fight each other for the magical 
stone, Citrine. The people of Nexus started to kill each other. 
The world of Nexus was at war. However, the magical stone was kept
safe by the people of Arkdemn. The people of Arkdemn were the
protectors of the magical stone.""")
time.sleep(10)
print()
end = input("Press enter to close the book...")
clearOutput(13)

print("You closed the book and put it back on the table.")
time.sleep(5)
clearOutput(1)

print("The voice says,")
time.sleep(1.5)
print()
print('"I see that you have read the book."')
time.sleep(5)
clearOutput(3)

print("You reply,")
time.sleep(1.5)
print()
print('"Yes, I have. So, what do I do now?."')
time.sleep(5)
clearOutput(3)

print("The voice replies,")
time.sleep(1.5)
print()
print('"You must go to the capital of Arkdemn and defend the magical stone, Citrine."')
time.sleep(5)
clearOutput(3)

print("You go outside and see a sword and a shield with a crest.")
time.sleep(2)
print()
print("You take the sword and shield.")
time.sleep(5)
clearOutput(3)

print("As you wander, you find out that you were already in the capital of Arkdemn.")